from io import TextIOWrapper
from types import CodeType
from pathlib import Path
from typing import Union

from bytecode import Instr, Bytecode
from lark import Lark, Token, Discard

from . import CodeGen

__all__ = ("TELEBASIC_GRAMMAR", "compile")

with open(Path(__file__).absolute().parent.parent / "telebasic.lark") as inf:
    TELEBASIC_GRAMMAR = Lark(inf.read(), start="start", propagate_positions=True)


def compile(source: Union[str, TextIOWrapper]) -> CodeType:
    """Compile some source into CPython code."""
    if isinstance(source, TextIOWrapper):
        body = source.read()
    else:
        body = source

    # TODO: Error reporting.
    tree = TELEBASIC_GRAMMAR.parse(body)

    with CodeGen() as gen:
        gen.transform(tree)

    return gen.compile()
