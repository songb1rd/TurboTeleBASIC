from types import CodeType
from typing import Any, List

from .remap import LabelRemapper
from .grammars import TELEBASIC_GRAMMAR


class ModuleBuilder:
    __slots__ = ("__includes", "__section", "__labels", "__paths", "__source")

    def __init__(self, section: str):
        self.__includes = {"relative": set(), "standard": set()}
        self.__paths = {}
        self.__labels = {}
        self.__source = []
        self.__section = section

    def __repr__(self) -> str:
        name = f"{type(self).__name__}"

        def get(attr: str) -> Any:
            return (
                getattr(self, f"_{name}{attr}")
                if attr.startswith("__") and not attr.endswith("__")
                else getattr(self, attr)
            )

        parts = ", ".join(f"{name}={get(name)!r}" for name in self.__slots__)
        return f"<{name}: {parts}>"

    def __enter__(self) -> "ModuleBuilder":
        return self

    def __exit__(self, *_):
        pass

    # Properties

    @property
    def section(self):
        return self.__section

    @property
    def labels(self):
        return self.__labels

    @property
    def paths(self):
        return self.__paths

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, val: List[str]):
        self.__source = val

    # Public API

    def remap_at(self, base: int):
        mapper = LabelRemapper(self, base)
        tree = TELEBASIC_GRAMMAR.parse(self.dump_source())

        labels = ControlFlowGraph().visit(tree).report()

        mapper.transform(tree)

        print(tree)

        # for diff in mapper.diff():
        #     pass

    def dump_source(self) -> str:
        lines = []
        for key in sorted(self.__source.keys()):
            lines.append(self.__source[key])

        return "\n".join(lines) + "\n"

    def include(self, ty: str, name: str) -> str:
        name = f".text.{ty}.{name}"
        builder = ModuleBuilder(name)
        self.__includes[ty].add(builder)
        return name, builder

    def produce(self) -> CodeType:
        return
        # TODO: produce the post processed source body
        # TODO: Error reporting.
        # tree = TELEBASIC_GRAMMAR.parse(body)

        # with CodeGen() as gen:
        #     gen.transform(tree)

        # return gen.compile()
