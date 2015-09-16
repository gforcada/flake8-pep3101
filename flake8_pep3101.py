# -*- coding: utf-8 -*-
import re


OLD_RE = re.compile(r'^(?:[^\'"]*[\'"][^\'"]*[\'"])*\s*%|^\s*%')


class Flake8Pep3101(object):
    """
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
        with open(self.filename) as f:
            for lineno, line in enumerate(f, start=1):
                found = OLD_RE.search(line)
                if found:
                    position = line.find('%')
                    msg = self.message.format(line[position:position + 2])
                    yield lineno, position, msg, type(self)
