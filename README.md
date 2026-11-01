# Flake8 PEP 3101 plugin

Python has three string formatting options:

- the old percent operator
- the `.format()` string method
- [f-strings](https://peps.python.org/pep-0498/) (only since python 3.6+)

Although f-strings are more ergonomic,
there a certain scenarios where the `.format()` method
is still the only viable option.

See [pyformat website](https://pyformat.info)
for examples of the percent operator vs the `format()` method.

For a more format definition see the [PEP 3101](https://www.python.org/dev/peps/pep-3101).

This plugin is based on a python checker
that was in [plone.recipe.codeanalysis](https://pypi.python.org/pypi/plone.recipe.codeanalysis).

## Install
-------
Install with pip:

```shell
pip install flake8-pep3101
```

## Requirements

- Python 3.11+ and pypy3
- flake8

## Extras

If you want to check whether your new style formatting are correctly defined,
check [flake8-string-format](https://pypi.python.org/pypi/flake8-string-format)
plugin.

## License

GPL 2.0
