# -*- coding: utf-8 -*-
from flake8_pep3101 import Flake8Pep3101
from tempfile import mkdtemp

import os
import unittest


class TestFlake8Pep3101(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_old_formatter(self):
        file_path = self._given_a_file_in_test_dir(
            'b = 3\n'
        )
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_new_formatting_no_problem(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello {0:s}".format("world")',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_s_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'b = 3',
            'print("hello %s" % ("world")\n',
            'import os3',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 13)
        self.assertEqual(ret[0][2], 'S001 found %s formatter')

    def test_i_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %i" % ("world")',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 13)
        self.assertEqual(ret[0][2], 'S001 found %i formatter')

    def test_p_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %p" % ("world")',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 13)
        self.assertEqual(ret[0][2], 'S001 found %p formatter')

    def test_r_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %r" % (self)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 13)
        self.assertEqual(ret[0][2], 'S001 found %r formatter')

    def test_multiline_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %s"',
            '% (self)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 0)
        self.assertEqual(ret[0][2], 'S001 found % formatter')

    def test_multiline_aligned_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'print("hello %s"',
            '      % (self)',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 6)
        self.assertEqual(ret[0][2], 'S001 found % formatter')

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
        self.assertEqual(ret[0][1], 14)
        self.assertEqual(ret[0][2], 'S001 found % formatter')


if __name__ == '__main__':
    unittest.main()
