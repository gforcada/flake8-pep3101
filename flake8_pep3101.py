# -*- coding: utf-8 -*-
import ast


class Flake8Pep3101(object):

    name = 'flake8_pep3101'
    version = '1.1'
    message = 'S001 found module formatter'

    def __init__(self, tree, filename):
        self.filename = filename
        self.tree = tree

    def run(self):
        if self.filename is 'stdin':
            tree = self.tree
        else:
            with open(self.filename) as f:
                tree = ast.parse(f.read())

        for stmt in ast.walk(tree):
            if isinstance(stmt, ast.BinOp) and \
                    isinstance(stmt.op, ast.Mod) and \
                    isinstance(stmt.left, (ast.Str, ast.Name)):
                yield stmt.lineno, stmt.col_offset, self.message, type(self)
