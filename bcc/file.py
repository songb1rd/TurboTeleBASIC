import sys
import re
import shlex
from dataclasses import dataclass
from typing import Dict, Union, List, Optional
from pathlib import Path

__all__ = ["File", "FileContents"]

FileContents = Dict[int, Union[str, "File"]]

_RE_NAME = re.compile(r"[a-zA-Z]+[$%#]?")
_RE_CODE_LABEL = re.compile(r"{([a-zA-Z_][a-zA-Z_0-9]*)}")


@dataclass
class File:
    mapping: FileContents
    path: Path

    def __str__(self) -> str:
        output = "\n".join(
            part.strip() if isinstance(part, str) else str(part)
            for _, part in self.mapping.items()
        )

        return output.strip()

    def remove_comments(self, *, recursive: bool = False):
        def is_code(line: str) -> bool:
            return bool(trimmed := line.strip()) and not trimmed.startswith("REM")

        def check(value: Union[str, "File"]) -> bool:
            if isinstance(value, str):
                return is_code(value)

            if isinstance(value, list):
                value[:] = [line for line in value if is_code(line)]

            elif recursive:
                value.remove_comments(recursive=recursive)

            return True

        self.mapping = {
            n: value
            for n, value in self.mapping.items()
            if check(value)
        }

    def flatten(self, *, buf: List[Union[str, "File"]] = None) -> "File":
        """"""
        output: List[Union[str, "File"]]
        output = buf or []

        for key in sorted(self.mapping):
            line = self.mapping[key]

            if isinstance(line, File):
                line.flatten(buf=output)
            else:
                assert isinstance(line, str)
                output.append(line)

        mapping: FileContents = dict(enumerate(output))

        return File(mapping=mapping, path=self.path)

    def normalize(self, label_mapping: Dict[str, str], cursor: int):
        """Normalize the output code.

            * Convert number-less lines into numbered lines
            * Coerce every numbered line into label form
            * Substitute GOTO/GOSUB destination with coerced label form
        """

        def fmt_ephemeral(n: int) -> str:
            return "{_line_0x%s}" % hex(n).upper()[2:]

        proto_ephemeral: Optional[str]

        for (index, entry) in self.mapping.items():
            if isinstance((file := entry), File):
                file.normalize(label_mapping=label_mapping, cursor=cursor)
                del file
                continue

            assert isinstance(entry, str)

            source = entry.strip()

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
