.. -*- coding: utf-8 -*-

Changelog
=========

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
