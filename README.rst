===============================
exception
===============================


.. image:: https://img.shields.io/pypi/v/exception.svg
        :target: https://pypi.python.org/pypi/exception

.. image:: https://img.shields.io/travis/tdhopper/exception.svg
        :target: https://travis-ci.org/tdhopper/exception

.. image:: https://readthedocs.org/projects/exception/badge/?version=latest
        :target: https://exception.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/tdhopper/cookiecutter-django/shield.svg
     :target: https://pyup.io/repos/github/tdhopper/exception/
     :alt: Updates


Extract unique Python-Exceptions with their traceback from a log file.

## WARNING!

The extraction logic here is heuristic and may fail you. Don't depend on it for any life or death situations. Also, please submit feedback on how it could be improved!

## Installational

 Clone this repository and install with

    python setup.py install

This adds a utility called `exception` or `exception.exe` to your path.

## Usage

To extract the Python tracebacks from a log called _logfile.txt_, run:

    $ exception -f logfile.txt

If you want to exclude certain exceptions, try:

    $ exception -f logfile.txt -e ValueError,AttributeError

You can all pass multiple filenames:

    $ exception -f logfile1.txt logfile2.txt

This would exclude would exclude any ``ValueError`` or ``AttributeError`` tracebacks from the output.

The tool can also read the log file from stdout, e.g.:

    cat logfile.txt | exception

or

    cat logfile.txt | exception -e ValueError


Credits
---------


This is based on [a script](https://gist.github.com/originell/1923003) by [@originell](https://github.com/originell).

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

