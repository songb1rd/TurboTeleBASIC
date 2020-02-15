from lark import v_args, Transformer


@v_args(tree=True)
class LabelRemapper(Transformer):
    def __init__(self, builder, base, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__builder = builder
        self.__base = base

    def label(self, tree):
        print(":", tree)
        return tree
