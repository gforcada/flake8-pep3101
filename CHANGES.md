# Changelog

## 3.1.1 (unreleased)


- Nothing changed yet.


## 3.1.0 (2026-11-01)

- update supported python versions (3.11 to 3.15) @gforcada

- improve CI speed by using `uvx` and `prek` @gforcada

- tighten GHA with `zizmor` @gforcada

## 3.0.0 (2025-10-25)

- drop python 3.8 support and add Python 3.13 support @gforcada

- drop python 3.9 support and add Python 3.14 support @gforcada

- bump pypy minimum version to 3.10.

## 2.1.0 (2023-11-03)

- drop python 3.7 support @gforcada

- test against python 3.12 @gforcada

- use `pyproject.toml` rather than `setup.py` @gforcada

- switch from `setuptools` to `hatchling` @gforcada

- switch to `main` branch @gforcada

- use `tox` and `pre-commit` to ease project maintenance @gforcada

## 2.0.0 (2022-10-08)

- update dependencies @gforcada

- test the code on GitHub actions @gforcada

- drop python 2.7 and only support python 3.7+ @gforcada

- use linters and formatters to keep code sane and beautiful @gforcada

- simplify the amount of code to write a test @gforcada

## 1.3.0 (2019-12-15)

- warn about `"string %i" % 33` which was previously ignored.
  Reported by @unformatt @gforcada

## 1.2.1 (2018-04-05)

- fix text on the error message @icemac

## 1.2 (2017-12-12)

- handle when there are numbers in either side of the modulo operator @gforcada

## 1.1 (2017-05-12)

- handle variable formatting (i.e. `my_string_variable % ('one', 'two', )`) @gforcada

- test against Python 3.6 @gforcada

- release universal wheels as well @gforcada

## 1.0 (2016-11-27)

- remove `tox` and use plain travis matrix to test @gforcada

- test on python 2.7, python 3.5, pypy and pypy3 @gforcada

- require `flake8` 3.0 @gforcada

- use ast to analyze the code.
  The regular expression used so far was mostly a hit or miss,
  with each corner case making it even more difficult to read.
  The new checker with ast is simple, elegant and so much easy to read @gforcada

## 0.6 (2016-10-29)

- handle edge case when a single or double quoted string
  has another pair of quotes inside ('lala "lu" la') with
  some % symbol inside as well @gforcada

## 0.5 (2016-10-26)

- add all possible string formatters @gforcada

- fix extension to work with flake8 > 3.0 @gforcada

- fix crash when the % symbol was the last character of a line @gforcada

## 0.4 (2016-07-03)

- rename pep8 to pycodestyle @alefteris

- add support for python 3.5 @alefteris

- add flake8 pypi classifier @alefteris

- drop python 3.3 and 3.4 support (only testing it probably works just fine) @gforcada

- fix travis and coveralls to work properly with python 3.5 @gforcada

## 0.3 (2016-03-05)

- allow stdin processing, this way text editor can pass input to flake8 @mjacksonw

## 0.2 (2015-09-16)

- 0.1 was a brown bag release @gforcada

## 0.1 (2015-09-16)

- initial release @gforcada

- create the `flake8` plugin per se @gforcada
