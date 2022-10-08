.. -*- coding: utf-8 -*-

Changelog
=========

2.0.0 (2022-10-08)
------------------

- Update dependencies. [gforcada]

- Test the code on GitHub actions. [gforcada]

- Drop python 2.7 and only support python 3.7+. [gforcada]

- Use linters and formatters to keep code sane and beautiful. [gforcada]

- Simplify the amount of code to write a test. [gforcada]

1.3.0 (2019-12-15)
------------------

- Warn about `"string %i" % 33` which was previously ignored.
  Reported by @unformatt.
  [gforcada]


1.2.1 (2018-04-05)
------------------

- Fix text on the error message.
  [icemac]

1.2 (2017-12-12)
----------------

- Handle when there are numbers in either side of the modulo operator.
  [gforcada]

1.1 (2017-05-12)
----------------

- Handle variable formatting (i.e. ``my_string_variable % ('one', 'two', )``).
  [gforcada]

- Test againsta Python 3.6.
  [gforcada]

- Release universal wheels as well.
  [gforcada]

1.0 (2016-11-27)
----------------
- Remove tox and use plain travis matrix to test.
  [gforcada]

- Test on python 2.7, python 3.5, pypy and pypy3.
  [gforcada]

- Require flake8 3.0.
  [gforcada]

- Use ast to analyze the code.
  The regular expression used so far was mostly a hit or miss,
  with each corner case making it even more difficult to read.
  The new checker with ast is simple, elegant and so much easy to read.
  [gforcada]

0.6 (2016-10-29)
----------------
- Handle edge case when a single or double quoted string
  has another pair of quotes inside ('lala "lu" la') with
  some % symbol inside as well.
  [gforcada]

0.5 (2016-10-26)
----------------
- Add all possible string formatters.
  [gforcada]

- Fix extension to work with flake8 > 3.0.
  [gforcada]

- Fix crash when the % symbol was the last character of a line.
  [gforcada]

0.4 (2016-07-03)
----------------
- Rename pep8 to pycodestyle.
  [alefteris]

- Add support for python 3.5.
  [alefteris]

- Add flake8 pypi classifier.
  [alefteris]

- Drop python 3.3 and 3.4 support (only testing it probably works just fine).
  [gforcada]

- Fix travis and coveralls to work properly with python 3.5.
  [gforcada]

0.3 (2016-03-05)
----------------
- Allow stdin processing, this way text editor can pass input to flake8.
  [mjacksonw]

0.2 (2015-09-16)
----------------
- 0.1 was a brown bag release.
  [gforcada]

0.1 (2015-09-16)
----------------
- Initial release
  [gforcada]

- Create the flake8 plugin per se.
  [gforcada]
