# -*- coding: utf-8 -*-
import re

try:
    import pycodestyle
except ImportError:
    import pep8 as pycodestyle

OLD_RE = re.compile(r'^(?:[^\'"]*[\'"][^\'"]*[\'"])*\s*%|^\s*%')


class Flake8Pep3101(object):
    """
    @do3cc:
    Checking for old style formatting is hard in the real world.
    The logging module does not support PEP3101 yet, but then again,
    you are not supposed to give the formatted string but the
    format string and the parameters to be inserted.
    I never found a reference for that but now sentry relies on it.
    So this check, looks for:
    1. two string delimiter characters following any number of whitespace and %
    2. Beginning of line, any number of whitespace and %

    This will ignore log messages that do not do inline message formatting,
    and it will find multiline old style log formatting.

    It will create false positives if you use % as a modulo operator
    and calculation spans multiple lines with the modulo character beginning
    a new line.
    """

    name = 'flake8_pep3101'
    version = '0.1'
    message = 'S001 found {0:s} formatter'

    def __init__(self, tree, filename):
        self.filename = filename

    def run(self):
        if self.filename is 'stdin':
            f = pycodestyle.stdin_get_value().splitlines()
        else:
            with open(self.filename) as fi:
                f = fi.read().splitlines()

        for lineno, line in enumerate(f, start=1):
            found = OLD_RE.search(line)
            if found:
                position = line.find('%')
                formatter = line[position:position + 2]
                if formatter[1] in ('p', 's', 'i', 'r'):
                    msg = self.message.format(formatter)
                else:
                    msg = self.message.format('%')

                yield lineno, position, msg, type(self)
