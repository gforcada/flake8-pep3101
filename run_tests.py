# -*- coding: utf-8 -*-
from flake8_pep3101 import Flake8Pep3101
from tempfile import mkdtemp

import os
import unittest


class TestFlake8PloneAPI(unittest.TestCase):

    def _given_a_file_in_test_dir(self, contents):
        test_dir = os.path.realpath(mkdtemp())
        file_path = os.path.join(test_dir, 'test.py')
        with open(file_path, 'w') as a_file:
            a_file.write(contents)

        return file_path

    def test_no_old_formatter(self):
        file_path = self._given_a_file_in_test_dir('b = 3\n')
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 0)

    def test_new_formatting_no_problem(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello {0:s}".format("world")',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())

    def test_s_formatter(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            'b = 3',
            'a = "something %s" % b',
            'import os3',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 2)
        self.assertEqual(ret[0][1], 15)
        self.assertEqual(ret[0][2], 'S001 found %s formatter')




    def test_analysis_should_return_false_for_invalid__s(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello %s" % ("world")',
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())

    def test_analysis_should_return_false_for_invalid__i(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello %i" % ("world")',  # noqa
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())

    def test_analysis_should_return_false_for_invalid__p(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello %p" % ("world")',  # noqa
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())

    def test_analysis_should_return_false_for_invalid__r(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello %r" % (self)',  # noqa
        ]))
        checker = Flake8Pep3101(None, file_path)
        ret = list(checker.run())

    def test_analysis_should_return_false_for_multiline_invalid(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'print("hello %s"',
            '% (self)',
        ]))
        with OutputCapture():
            self.assertFalse(PEP3101(self.options).run())

    def test_analysis_its_complicated(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'log("%s is bad", "me")'
        ]))
        with OutputCapture():
            self.assertTrue(PEP3101(self.options).run())

    def test_analysis_its_complicated2(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            '"""""""1" if "%" else "2"'
        ]))
        with OutputCapture():
            self.assertTrue(PEP3101(self.options).run())

        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            '"""""""1" if "%" else "2%s" % "x"'
        ]))
        with OutputCapture():
            self.assertFalse(PEP3101(self.options).run())

    def test_analysis_should_return_true_for_logs(self):
        file_path = self._given_a_file_in_test_dir('\n'.join([
            '# -*- coding: utf-8 -*-',
            'console.log("hello %s", "world")',  # noqa
        ]))
        with OutputCapture():
            self.assertTrue(PEP3101(self.options).run())


if __name__ == '__main__':
    unittest.main()
