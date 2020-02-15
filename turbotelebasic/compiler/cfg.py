from lark import Visitor

class ControlFlowGraph(Visitor):
    def label(self, tree):
        print(":", tree)
        return tree
