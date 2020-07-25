import sys
import pathlib

try:
    import bcc
except ImportError:
    path = pathlib.Path(".").parent.resolve().absolute()
    sys.path.insert(0, f"{path!s}")
    del path

    import bcc

from bcc.file import File

DEFINES = """
#define true 1
#define the_truth 42
#define false 0
#undef the_truth
"""

def test_context_define():
    source = dict(enumerate(DEFINES.split("\n")))
    source_file = File(mapping=source, path=pathlib.Path("."))

    context = bcc.preproc.process(source_file)

    assert {"true": "1", "false": "0"} == context.labels
