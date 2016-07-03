.. -*- coding: utf-8 -*-

.. image:: https://travis-ci.org/gforcada/flake8-pep3101.svg?branch=master
   :target: https://travis-ci.org/gforcada/flake8-pep3101

.. image:: https://coveralls.io/repos/gforcada/flake8-pep3101/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/gforcada/flake8-pep3101?branch=master

Flake8 PEP 3101 plugin
======================
Python has two string formatting options,
either the old percent operator or the new ``.format()`` string method.

Being the new one more powerful, expressive and a drop-in replacement
over the old one.

See `pyformat website`_ for lots of examples of old vs new formatting.

For a more format definition see the `PEP 3101`_.

This plugin is based on a python checker that was in `plone.recipe.codeanalysis`_.

Install
-------
Install with pip::

    $ pip install flake8-pep3101

Requirements
------------
- Python 2.7, 3.5
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
.. _`flake8-string-format`: https://pypi.python.org/pypi/flake8-string-format
.. _`plone.recipe.codeanalysis`: https://pypi.python.org/pypi/plone.recipe.codeanalysis
