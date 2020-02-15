from io import TextIOWrapper
from pathlib import Path
from typing import Union, Iterator, List

from lark import Lark


__all__ = ("iter_split", "read_grammar", "flatten")

def iter_split(source: Union[str, TextIOWrapper], delim: str) -> Iterator[str]:
    if isinstance(source, TextIOWrapper):
        for line in source:
            yield line
        return

    assert isinstance(source, str)
    bucket: List[str] = []

    for ch in source:
        if ch == delim:
            yield "".join(bucket)
            bucket = []
        else:
            bucket.append(ch)
    else:
        if bucket:
            yield "".join(bucket)


def read_grammar(file: str, start: str) -> Lark:
    with open(Path(__file__).absolute().parent / file) as inf:
        return Lark(inf.read(), start=start, propagate_positions=True)


def flatten(seq):
    if not seq:
        return seq

    if isinstance(seq[0], list):
        return flatten(seq[0]) + flatten(seq[1:])

    return seq[:1] + flatten(seq[1:])
