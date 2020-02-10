from io import TextIOWrapper
from pathlib import Path
from typing import Dict, List

import click
from click import File

from .compiler import compile


@click.command()
@click.argument("input_file", type=File("r"), required=False)
@click.option("-i", "--interpret", is_flag=True)
def main(*, input_file: TextIOWrapper, interpret: bool):
    """TuboTeleBASIC entry point."""
    code_object = compile(input_file)

    from dis import dis

    dis(code_object)

    if interpret:
        exec(code_object)

if __name__ == "__main__":
    main()
