from ..utils import read_grammar, iter_split


TELEBASIC_GRAMMAR = read_grammar("telebasic.lark", "start")
TURBOBASIC_GRAMMAR = read_grammar("turbobasic.lark", "directives")
