import logging
from io import TextIOWrapper
from pathlib import Path

import click
from click import File
from lark import Lark

logging.basicConfig(level=logging.DEBUG)

with open(Path(__file__).absolute().parent / "telebasic.lark") as inf:
    TELEBASIC_GRAMMAR = inf.read()

@click.command()
@click.argument("input_file", type=File("r"), required=False)
def main(input_file: TextIOWrapper):
    """TuboTeleBASIC entry point."""
    p = Lark(TELEBASIC_GRAMMAR, start="start", parser='lalr', debug=True)
    print(p.parse(input_file.read()))

if __name__ == "__main__":
    main()
