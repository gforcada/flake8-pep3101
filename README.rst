.. -*- coding: utf-8 -*-

.. image:: https://github.com/gforcada/flake8-pep3101/actions/workflows/testing.yml/badge.svg?event=push
   :target: https://github.com/gforcada/flake8-pep3101/actions/workflows/testing.yml

.. image:: https://coveralls.io/repos/gforcada/flake8-pep3101/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/gforcada/flake8-pep3101?branch=master

Flake8 PEP 3101 plugin
======================
Python has three string formatting options:

- the old percent operator
- the ``.format()`` string method
- `f-strings`_ (only since python 3.6+)

Although f-strings are more ergonomic, there a certain scenarios where the
``.format()`` method is still the only viable option.

See `pyformat website`_ for examples of the percent operator vs the ``format()`` method.

For a more format definition see the `PEP 3101`_.

This plugin is based on a python checker that was in `plone.recipe.codeanalysis`_.

Install
-------
Install with pip::

    $ pip install flake8-pep3101

Requirements
------------
- Python 3.7, 3.8, 3.9, 3.10 and pypy3
- flake8

Extras
------
If you want to check whether your new style formatting are correctly defined,
check `flake8-string-format`_ plugin.

License
-------
GPL 2.0

.. _`pyformat website`: https://pyformat.info
.. _`PEP 3101`: https://www.python.org/dev/peps/pep-3101
.. _`f-strings`: https://peps.python.org/pep-0498/
.. _`flake8-string-format`: https://pypi.python.org/pypi/flake8-string-format
.. _`plone.recipe.codeanalysis`: https://pypi.python.org/pypi/plone.recipe.codeanalysis
