from io import TextIOWrapper
from types import CodeType
from typing import Union, Tuple, Iterator

from . import CodeGen
from .builder import ModuleBuilder
from .parse import parse

__all__ = ("compile",)


def compile(source: Union[str, TextIOWrapper]) -> CodeType:
    """Compile some source into CPython code."""
    with parse(source, section=".text") as builder:
        pass
