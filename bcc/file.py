import sys
import re
import shlex
from dataclasses import dataclass
from typing import Dict, Union, List
from pathlib import Path

__all__ = ["File"]

Block = List[str]
FileContents = Dict[int, Union[str, "File", Block]]

_RE_NAME = re.compile(r"[a-zA-Z]+[$%#]?")
_RE_CODE_LABEL = re.compile(r"{([a-zA-Z_][a-zA-Z_0-9]*)}")


@dataclass
class File:
    mapping: FileContents
    path: Path

    def remove_comments(self, *, recursive: bool = False):
        def is_code(line: str) -> bool:
            return bool(trimmed := line.strip()) and not trimmed.startswith("REM")

        def check(value: FileContents):
            if isinstance(value, str):
                return is_code(value)

            if isinstance(value, list):
                value[:] = [line for line in value if is_code(line)]

            elif recursive:
                value.remove_comments(recursive=recursive)

            return True

        self.mapping = {n: value for n, value in self.mapping.items() if check(value)}

    def flatten(self, *, buf: List[str] = None):
        output = buf or []

        keys = sorted(self.mapping.keys())
        for key in keys:
            line = self.mapping[key]

            if isinstance(line, File):
                line.flatten(buf=output)
                continue

            output.append(line)

        mapping = dict(enumerate(output))

        return File(mapping=mapping, path=self.path)

    def normalize(self, label_mapping: Dict[str, str], cursor: int):
        """Normalize the output code.

            * Convert number-less lines into numbered lines
            * Coerce every numbered line into label form
            * Substitute GOTO/GOSUB destination with coerced label form
        """
        def fmt_ephemeral(n: int) -> str:
            return "{_line_0x%s}" % hex(n).upper()[2:]

        for (index, source) in self.mapping.items():
            if isinstance(source, File):
                source.normalize(label_mapping=label_mapping, cursor=cursor)
                continue

            source = source.strip()

            if " " not in source:
                source = f" {source}"

            head, rest = source.split(" ", maxsplit=1)

            if not head:  # Implicit numbering
                head = str(cursor)
                assert re.fullmatch(r"\d+", head) is not None
                cursor += 1

            match = re.fullmatch(r"\d+", head)

            if match is not None:
                proto_ephemeral = fmt_ephemeral(int(match[0]))

            elif _RE_CODE_LABEL.fullmatch(head) is None:
                rest = f"{head} {rest}"
                head = str(cursor)

                assert re.fullmatch(r"\d+", head) is not None

                proto_ephemeral = fmt_ephemeral(cursor)

                cursor += 1
            else:
                proto_ephemeral = None


            while (match := re.search(r"GO(TO|SUB) (\d+)", rest)) is not None:
                to_sub, dest, = match[1], match[2]
                ephemeral = fmt_ephemeral(int(dest))

                rest = re.sub(f"GO{to_sub} {dest}", f"GO{to_sub} {ephemeral}", rest)
                label_mapping[ephemeral] = dest

            normalized = f"{proto_ephemeral or head} {rest}".strip()

            if self.mapping[index] != normalized:
                self.mapping[index] = normalized

            if proto_ephemeral is not None:
                label_mapping[proto_ephemeral] = head
