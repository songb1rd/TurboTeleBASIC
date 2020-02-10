from ast import literal_eval
from types import CodeType

from bytecode import Instr, Bytecode
from lark import Lark, Token, Discard, v_args, Tree
from lark.visitors import Visitor, Transformer

__all__ = ("CodeGen",)


def flatten(seq):
    if not seq:
        return seq

    if isinstance(seq[0], list):
        return flatten(seq[0]) + flatten(seq[1:])

    return seq[:1] + flatten(seq[1:])

@v_args(tree=True)
class CodeGen(Transformer):
    __flag = False

    def __enter__(self):
        self.__flag = True
        self.__code: Dict[Optional[int], List[Union[Instr, Tree]]] = {None: []}
        self.__label_cursor: Optional[int] = None
        self.__string_table: List[str] = []
        return self

    def __exit__(self, *_):
        assert self.__flag, "Flag was not set by `__enter__`, how did we get called?"

        self.__code[self.__label_cursor].extend(self.__code[None])
        self.__code[None] = []

    # Public api

    def compile(self) -> CodeType:
        instructions = []
        code = self.__code.copy()
        code.pop(None)

        for label in sorted(code.keys()):
            blocks = code[label]

            for entity in blocks:
                if isinstance(entity, Tree):
                    block = entity.children
                else:
                    block = entity

                assert isinstance(block, list)

                if not block:
                    continue

                assert all(
                    isinstance(part, Instr) for part in block
                ), f"Not all blocks have been transformed. ({code[label]!r}"

                instructions.extend(block)

        instructions.extend([Instr("LOAD_CONST", None), Instr("RETURN_VALUE")])

        bytecode = Bytecode(instructions)
        return bytecode.to_code()

    # Transformers

    def line(self, tree):
        assert tree.children

        first, *rest = tree.children

        if not isinstance(first, Token) and first.data == "label":
            assert len(first.children) == 1

            label, *_ = first.children
            assert isinstance(label, Token)

            if self.__code[None]:
                self.__code[self.__label_cursor].extend(self.__code[None])
                self.__code[None] = []

            self.__label_cursor = label.value

            print("LINE", label.value, rest)
            self.__code[label.value] = rest
        else:
            # Matched lines that dont have a starting label
            # Are typical cases of inline separated lines e.g:
            # ``00 PRINT: PRINT: INPUT A$``
            self.__code[None].extend(tree.children)

        return tree

    def string(self, tree):
        assert tree.children
        assert isinstance(tree.children[0], Token)
        return Instr("LOAD_CONST", tree.children[0].value)

    def expr_rhs(self, tree):
        print(">", tree)
        return tree

    def expr(self, tree):

        for index, child in enumerate(tree.children):
            print(child, type(child))
            if isinstance(child, Token):
                if child.type == "NUMBER":
                    tree.children[index] = Instr("LOAD_CONST", child.value)

            elif isinstance(child, Tree):
                if child.data == "expr_rhs":
                    op, *rest = child.children
                    tree.children[index] = [*rest, op]

        print("@", tree)
        return tree.children

    def ADD(self, tree):
        return Instr("BINARY_ADD")

    def SUB(self, tree):
        return Instr("BINARY_SUBTRACT")

    def MUL(self, tree):
        return Instr("BINARY_MULTIPLY")

    def print(self, tree):
        print("PRINT", tree)

        nargs = len(tree.children)

        children = flatten(tree.children.copy())
        print(children)

        tree.children = [
            Instr("LOAD_NAME", "print"),
            *children,
            Instr("CALL_FUNCTION", nargs),
        ]

        return tree


    def NUMBER(self, token):
        assert isinstance(token, Token)
        return token.update(value=literal_eval(token))

    def WS_INLINE(self, _):
        assert isinstance(_, Token)
        raise Discard

    WS = WS_INLINE
