import ast
import textwrap
import unittest
from unittest import mock

from flake8_pep3101 import Flake8Pep3101


class NewTestFlake8Pep3101(unittest.TestCase):
    def check_code(self, source, expected_codes=None):
        """Check if the given source code generates the given flake8 errors

        If `expected_codes` is a string is converted to a list,
        if it is not given, then it is expected to **not** generate any error.
        """
        if isinstance(expected_codes, str):
            expected_codes = [expected_codes]
        elif expected_codes is None:
            expected_codes = []
        tree = ast.parse(textwrap.dedent(source))
        checker = Flake8Pep3101(tree, '/home/script.py')
        return_statements = list(checker.run())

        self.assertEqual(
            len(return_statements), len(expected_codes), f'Got {return_statements}'
        )

        for item, code in zip(return_statements, expected_codes):
            self.assertTrue(
                item[2].startswith(f'{code} '),
                f'Actually got {item[2]} rather than {code}',
            )

    @mock.patch('flake8.utils.stdin_get_value')
    def test_stdin(self, stdin_get_value):
        source = 'a = "hello %s" % ("world")'
        stdin_get_value.return_value = source
        checker = Flake8Pep3101('', 'stdin')
        ret = list(checker.run())
        self.assertEqual(
            len(ret),
            1,
        )

    def test_no_old_formatter(self):
        source = 'b = 3'
        self.check_code(source)

    def test_new_formatter(self):
        source = 'print("hello {0:s}".format("world"))'
        self.check_code(source)

    def test_error(self):
        source = 'print("hello %s" % ("world"))'
        self.check_code(source, 'S001')

    def test_line_number(self):
        source = """
        a = 2
        open = 4
        msg = "hello %s" % ("world")
        """
        tree = ast.parse(textwrap.dedent(source))
        checker = Flake8Pep3101(tree, '/home/script.py')
        ret = list(checker.run())
        self.assertEqual(ret[0][0], 4)

    def test_offset(self):
        source = """
        def bla():
            msg = "hello %s" % ("world")
        """
        tree = ast.parse(textwrap.dedent(source))
        checker = Flake8Pep3101(tree, '/home/script.py')
        ret = list(checker.run())
        self.assertEqual(ret[0][1], 10)

    def test_s_formatter(self):
        source = 'print("hello %s" % (\'lo\'))'
        self.check_code(source, 'S001')

    def test_multiline_formatter(self):
        source = """
        print("hello %s"
        % ('world')
        )
        """
        self.check_code(source, 'S001')

    def test_multiline_aligned_formatter(self):
        source = """
        print("hello %s"
                     % ('world')
        )
        """
        self.check_code(source, 'S001')

    def test_logging_module(self):
        source = """
        import logging
        logger = logging.getLogger()
        logger.info("%s world", "hello")
        """
        self.check_code(source)

    def test_multiple_strings(self):
        source = '"""""""1" if "%" else "2"'
        self.check_code(source)

    def test_multiple_single_quotes_strings(self):
        source = "'''''''1' if '%' else '2'"
        self.check_code(source)

    def test_multiple_strings_with_old_formatting(self):
        """Check that multiple quoting is handled properly.

        In this case correctly detecting it.
        """
        source = '"""""""1" if "%" else "2%s" % "x"'
        self.check_code(source, 'S001')

    def test_percent_on_string(self):
        """Check that multiple quoting is handled properly.

        In this case no string substitution is happening.

        Found in plone.app.drafts.tests
        """

        source = 'a = \'"%2B%2Badd%2B%2BMyDocument"\''
        self.check_code(source)

    def test_percent_as_last_character_on_line(self):
        """Check that a percent symbol as the last character on a line is
        handled properly.
        """
        source = """
        a = 'my string %s %s' \
            % \
            ('3', '4', )
        """
        self.check_code(source, 'S001')

    def test_variable(self):
        source = """
        a = 'my string %s %s'
        a % ('3', '4', )
        """
        self.check_code(source, 'S001')

    def test_right_hand_number_modulo(self):
        source = """
        var = 40
        if var % 50 == 0:
            print(var)
        """
        self.check_code(source)

    def test_left_hand_number_modulo(self):
        source = """
        var = 40
        if 50 % var == 0:
            print(var)
        """
        self.check_code(source)

    def test_right_hand_string_left_hand_number(self):
        source = 'print("asd %s" % 1)'
        self.check_code(source, 'S001')

    def test_right_hand_string_left_hand_variable(self):
        source = """
        a = 44
        print("asd %s" % a)
        """
        self.check_code(source, 'S001')
