from io import TextIOWrapper
from re import compile as _re_compile, Pattern
from typing import Optional, Union, Tuple
from itertools import starmap, chain

from ..utils import read_grammar, iter_split
from .builder import ModuleBuilder
from .grammars import TELEBASIC_GRAMMAR, TURBOBASIC_GRAMMAR

__all__ = ("TELEBASIC_GRAMMAR", "TURBOBASIC_GRAMMAR", "parse")


_LINE_NUM_RE: Pattern = _re_compile(r"^(\d+)")
_PATTERN_RE: Pattern = _re_compile(r"#([a-z]+)(?:::([a-z]+))+")


def parse(
    source: Union[str, TextIOWrapper],
    *,
    section: str,
    builder: Optional[ModuleBuilder] = None
) -> ModuleBuilder:
    builder = builder or ModuleBuilder(section)

    def strip(index: int, st: str) -> Tuple[int, str]:
        return (index, st.strip())

    def truthful(pair: Tuple[int, str]) -> bool:
        _, st, = pair
        return bool(st)

    lines: Dict[int, str] = {}
    stream = filter(truthful, starmap(strip, enumerate(iter_split(source, "\n"))))

    # Parse directives.
    for index, line in stream:
        if line[0] != "#":
            lines[index] = line
            pushback = [(index, line)]
            break

        tree = TURBOBASIC_GRAMMAR.parse(line)

        assert tree.data == "directives"

        tree = tree.children[0]

        assert tree.children

        target = tree.children[1]

        ty, name = target.data, target.children[0].value

        assert ty in ("standard", "relative")

        include_section, include_builder = builder.include(ty, name)

        if ty == "standard":
            raise NotImplementedError("There is no std yet.")

        else:
            with open(f"{name}.bas") as inf:
                parse(inf, section=include_section)

    else:
        pushback = []

    # Parse paths
    for index, line in chain(pushback, stream):
        lines[index] = line

        match = _LINE_NUM_RE.match(line)

        assert match is not None

        label = int(match.group())

        builder.labels[label] = index

        line_paths = list(_PATTERN_RE.finditer(line))

        if not line_paths:
            continue

        builder.paths[label] = tuple(line_paths)

    builder.source = lines

    # print(builder.dump_source())
    print(builder.labels, builder.source, builder.paths)
    builder.remap_at(1000)

    return builder
