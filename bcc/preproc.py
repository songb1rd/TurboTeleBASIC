"""A classic C-like preprocessor.

Directive precedence ::

    * include
    * enum
    * define
    * undef
    * branch
    * switch
"""

import shlex
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Set, Callable, Optional, Any
from pathlib import Path

from . import File, FileContents

__all__ = ["Context"]

@dataclass
class Context:
    source: File = field(init=True, repr=False)
    labels: Dict[str, str] = field(default_factory=dict)
    included: List["File"] = field(default_factory=list)
    mapped: Dict[int, Tuple[str, List[str]]] = field(default_factory=dict)

    def process_include(self, line: int, include_path: str):
        path = self.source.path.parent.joinpath(include_path)

        with open(path) as included_file:
            mapping: FileContents = dict(enumerate(included_file))

        self.source.mapping[line] = file = File(mapping, path)
        self.included.append(file)

    def process_enum(self, line: int, *args):
        stem, _, = args
        sequence = sorted(list(self.source.mapping.keys()))
        end = line

        ticker = 0
        for key in sequence[line + 1:]:
            entry = self.source.mapping[key]
            assert isinstance(entry, str)
            source = entry.strip()  # type: ignore

            if source == "}":
                end = key
                break

            assert source[-1] == ",", f"Possibly missing COMMA \",\" on {line=!r}"

            source = source[:-1]

            if "=" in source:
                assert source.count("=") == 1, f"Expected only one EQUALS \"=\" on {line=!r}"
                leaf, value = source.split("=", maxsplit=1)
                value = value.strip()

                assert value.isdigit(), f"Enum values must only be digits. (Got {value=!r})"
                assert int(value) >= ticker, f"Can't reset enum values past previous."

                ticker = int(value)
                ticker += 1
            else:
                leaf = source
                value = f"{ticker}"
                ticker += 1

            self.source.mapping[key] = f"#define {stem}.{leaf} {value}"
            self.mapped[key] = ("define", [f"{stem}.{leaf}", f"{value}"])
        else:
            raise RuntimeError("Ran out of runway.")

        self.source.mapping[line] = ""
        self.source.mapping[end] = ""

    def process_define(self, line: int, *args):
        name, *rest = args

        self.labels[name.strip()] = " ".join(rest).strip()
        self.source.mapping[line] = ""

    def process_undef(self, line: int, *args):
        name, *_ = args

        self.labels.pop(name, None)
        self.source.mapping[line] = ""

    def process_switch(self, line: int, *args):
        subject, _, = args
        subject = subject.strip()

        sequence = sorted(list(self.source.mapping.keys()))
        for key in sequence[line + 1:]:
            source = self.source.mapping[key].strip()  # type: ignore

            if source == "}":
                end = key
                break

            assert "=>" in source, f"Missing fat arrow => on {line=!r}"

            target, branch, = source.split("=>", maxsplit=1)
            target = target.strip()
            branch = branch.strip()

            self.source.mapping[key] = f"IF {subject} = {target} THEN {branch}"
        else:
            raise RuntimeError("Ran out of runway.")

        self.source.mapping[line] = ""
        self.source.mapping[end] = ""

    def process_branch(self, line: int, *args):
        subject, _, = args
        subject = subject.strip()

        self.source.mapping[line] = f"#switch {subject} {{"
        self.mapped[line] = ("switch", args)  # type: ignore

        sequence = sorted(list(self.source.mapping.keys()))
        for key in sequence[line + 1:]:
            source = self.source.mapping[key].strip()  # type: ignore

            if source == "}":
                end = key
                break

            assert "=>" in source, f"Missing fat arrow => on {line=!r}"

            target, branch, = source.split("=>", maxsplit=1)
            target = target.strip()
            branch = branch.strip()

            self.source.mapping[key] = f"{target} => GOTO {branch}"
        else:
            raise RuntimeError("Ran out of runway.")

    def process_ifdef(self, line: int, *args):
        target, = args

        blocks = [(target, line)]

        start = line
        end = None
        else_found = False

        sequence = sorted(list(self.source.mapping))
        for key in sequence[line + 1:]:
            source = self.source.mapping[key].strip()  #type: ignore

            if source == "#endif":
                self.mapped.pop(key)

                end = key + 1
                break

            if source == "#else":
                self.mapped.pop(key)

                if else_found:
                    raise RuntimeError("Duplicate #else ...")

                blocks.append((None, key))
                continue

            if source == "#elif":
                self.mapped.pop(key)

                _, target, = shlex.split(source[1:])
                blocks.append((target, key))
                continue

        else:
            raise RuntimeError("Missing #endif ?")

        keep: Optional[Tuple[int, int]]
        for idx, (target, block_start) in enumerate(blocks):
            if target is None:
                keep = (block_start + 1, end - 1)
                break

            elif target in self.labels:
                _, block_end, = blocks[idx + 1]
                keep = (block_start + 1, block_end)
                break
        else:
            keep = None

        ifdef_span = set(range(start, end))

        if keep is not None:
            block_span = range(*keep)
            ifdef_span ^= set(block_span)
        else:
            block_span = range(0, 0)

        block_source: FileContents = {}

        for idx in block_span:
            block_source[idx] = self.source.mapping[idx]

        for idx in ifdef_span:
            self.source.mapping[idx] = ""

        for idx, source_, in block_source.items():
            self.source.mapping[idx] = source_


def scan(source: File) -> Dict[int, Tuple[str, List[str]]]:
    """Scan a source map for lines containing pre-processor directives."""
    directives = {}

    for n, line in source.mapping.items():
        assert isinstance(line, str)

        if (trimmed := line.strip()) and trimmed[0] == "#":
            assert trimmed[0] == "#", repr(trimmed)

            op, *args = shlex.split(trimmed[1:], posix=False)
            op = op.strip()

            directives[n] = (op, args)

    return directives


def process(
    source: File,
    *,
    include: bool = True,
    enum: bool = True,
    define: bool = True,
    undef: bool = True,
    branch: bool = True,
    switch: bool = True,
    ifdef: bool = True,
) -> Context:
    context = Context(source=source)
    scanned = scan(source)

    op: str
    args: List[str]

    for n, (op, args) in scanned.items():
        context.mapped[n] = (op, args)

    directives: Dict[str, Tuple[bool, Callable[..., Any]]]
    directives = {
        "ifdef": (ifdef, context.process_ifdef),
        "include": (include, context.process_include),
        "enum": (enum, context.process_enum),
        "define": (define, context.process_define),
        "undef": (undef, context.process_undef),
        "branch": (branch, context.process_branch),
        "switch": (switch, context.process_switch),
    }

    passes = [(op, func) for op, (flag, func) in directives.items() if flag]

    while context.mapped:
        in_order = sorted(context.mapped)

        for n in in_order:
            if (entry := context.mapped.pop(n, None)) is not None:
                # ifdef modifies the source mapping but context.mapped works off
                # an old scan result.
                #
                # When ifdef removes a line it just sets it to an empty string.
                # therefore we just check if the source mapping of line `n` is something.
                if not context.source.mapping.get(n, False):
                    continue

                op, args = entry
                _, handler, = directives[op]
                handler(n, *args)

    return context
