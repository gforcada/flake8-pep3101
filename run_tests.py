# -*- coding: utf-8 -*-
from flake8_pep3101 import Flake8Pep3101
from flake8.main import application
from tempfile import mkdtemp
from testfixtures import OutputCapture

import os
import unittest


class TestFlake8Pep3101(unittest.TestCase):

    @staticmethod
    def _given_a_file_in_test_dir(contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_old_formatter(self):
        file_path = self._given_a_file_in_test_dir(
            'b = 3\n'
        )
        app = application.Application()
        with OutputCapture() as output:
            app.run([file_path, ])

        self.assertEqual(
            output.captured,
            ''
        )

    def test_new_formatting_no_problem(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello {0:s}".format("world"))\n',
        ]))
        app = application.Application()
        with OutputCapture() as output:
            app.run([file_path, ])

        self.assertEqual(
            output.captured,
            ''
        )

    def test_s_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %s" % (\'lo\'))',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 6)
        self.assertEqual(ret[0][2], 'S001 found modulo formatter')

    def test_multiline_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %s"',
            '% (\'world\'))',
        ]))
        app = application.Application()
        with OutputCapture() as output:
            app.run([file_path, ])

        self.assertIn(
            '1:7: S001 found modulo formatter',
            output.captured
        )

    def test_multiline_aligned_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %s"',
            '      % (\'world\'))',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 6)
        self.assertEqual(ret[0][2], 'S001 found modulo formatter')

    def test_logging_module(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'import logging',
            'logger = logging.getLogger()',
            'logger.info("%s is bad", "me")'
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_multiple_strings(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '"""""""1" if "%" else "2"'
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_multiple_single_quotes_strings(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            "'''''''1' if '%' else '2'"
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_multiple_strings_with_old_formatting(self):
        """Check that multiple quoting is handled properly.

        In this case correctly detecting it.
        """
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '"""""""1" if "%" else "2%s" % "x"'
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 22)
        self.assertEqual(ret[0][2], 'S001 found modulo formatter')

    def test_percent_on_string(self):
        """Check that multiple quoting is handled properly.

        In this case no string substitution is happening.

        Found in plone.app.drafts.tests
        """
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'a = \'"%2B%2Badd%2B%2BMyDocument"\''
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_percent_as_last_character_on_line(self):
        """Check that a percent symbol as the last character on a line is
        handled properly.
        """
        file_path = self._given_a_file_in_test_dir('\n'.join([
            "a = 'my string %s %s' \\",
            "    %\\",
            "    ('3', '4', )",
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 4)
        self.assertEqual(ret[0][2], 'S001 found modulo formatter')

    def test_variable(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            "a = 'my string %s %s'",
            "a % ('3', '4', )",
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 0)
        self.assertEqual(ret[0][2], 'S001 found modulo formatter')

    def test_right_hand_number_modulo(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'var = 40',
            'if var % 50 == 0:',
            '    print(var)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_left_hand_number_modulo(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'var = 40',
            'if 50 % var == 0:',
            '    print(var)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_right_hand_string_left_hand_number(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("asd %s" % 1)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)

    def test_right_hand_string_left_hand_variable(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'a = 44',
            'print("asd %s" % a)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
