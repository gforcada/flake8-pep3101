import ast

from flake8 import utils as stdin_utils


class Flake8Pep3101:
    name = 'flake8_pep3101'
    version = '1.2.1'
    message = 'S001 found modulo formatter'

    def __init__(self, tree, filename):
        self.filename = filename
        self.tree = tree

    def run(self):
        tree = self.tree

        if self.filename == 'stdin':
            lines = stdin_utils.stdin_get_value()
            tree = ast.parse(lines)

        for stmt in ast.walk(tree):
            if self._is_module_operation(stmt):
                if self._is_left_hand_number(stmt):
                    continue
                if self._is_modulo_variable_and_number(stmt):
                    continue

                if isinstance(stmt.left, (ast.Str, ast.Name)):
                    yield (
                        stmt.lineno,
                        stmt.col_offset,
                        self.message,
                        type(self),
                    )

    @staticmethod
    def _is_module_operation(stmt):
        return isinstance(stmt, ast.BinOp) and isinstance(stmt.op, ast.Mod)

    @staticmethod
    def _is_left_hand_number(stmt):
        """Check if it is a case of `44 % SOMETHING`."""
        return isinstance(stmt.left, ast.Num)

    @staticmethod
    def _is_modulo_variable_and_number(stmt):
        """Check if it is a case of `var % 44`."""
        return isinstance(stmt.right, ast.Num) and isinstance(stmt.left, ast.Name)
