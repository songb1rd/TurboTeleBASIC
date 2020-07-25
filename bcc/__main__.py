import re

from . import preproc, File

_RE_NAME = re.compile(r"[a-zA-Z]+[$%#]?")
_RE_CODE_LABEL = re.compile(r"{([a-zA-Z_][\.a-zA-Z_0-9]*)}")


def main():
    step = 1
    starting_point = cursor = 0x00

    label_mapping = {}

    import sys

    input_file = sys.argv[1]

    with open(input_file) as inf:
        source_code = dict(enumerate(inf))
        output_code = source_code.copy()

    from pathlib import Path

    output_file = File(mapping=output_code, path=Path(input_file))

    def preprocess_recursively(file):
        contexts = [context := preproc.process(file)]

        for subfile in context.included:
            contexts.extend(preprocess_recursively(file=subfile))

        return contexts

    files = preprocess_recursively(output_file)

    for context in files:
        label_mapping.update(context.labels)


    output_file.remove_comments(recursive=True)

    def into_str(part):
        if isinstance(part, str):
            return part.strip()

        assert isinstance(part, File)

        part = "\n".join(into_str(part) for _, part in part.mapping.items())
        return part.strip()

    # Normalize output

    output_file.normalize(label_mapping=label_mapping, cursor=cursor)

    file = output_file.flatten()

    # Scan for labels

    labels = {}
    for n, item in file.mapping.items():
        assert isinstance(item, str), repr(item)

        if results := [match.group(1) for match in _RE_CODE_LABEL.finditer(item)]:
            labels[n] = results

    # Perform renumbering

    cursor = starting_point

    for (line, source) in file.mapping.items():
        assert not isinstance(source, File), repr(source)

        head, _ = source.split(" ", maxsplit=1)

        match = re.fullmatch(r"\d+", head)

        assert match is None

        if _RE_CODE_LABEL.fullmatch(head) is None:
            head = "{_line_0x%s}" % hex(cursor).upper()[2:]

        assert _RE_CODE_LABEL.fullmatch(head) is not None, f"{head=!r}, {source=!r}"

        label_mapping[head[1:-1]] = str(cursor)

        cursor += step

    # Fill the holes in the template

    for (line, source) in file.mapping.items():
        if line in labels:
            group = set(labels.pop(line))

            for label in group:
                pat = "{%s}" % label

                total = sum([1 for _ in re.finditer(pat, source)])

                digit = label_mapping[label]

                source, count, = re.subn(f"{{{label}}}", digit, source)

                assert count == total

        if source != file.mapping[line]:
            file.mapping[line] = source

    print(into_str(file))


if __name__ == "__main__":
    main()
