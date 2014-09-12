Extract unique Python-Exceptions with their Traceback from a log/text file.

Usage::

    python exceptional -f logfile.txt

Furthermore it supports excluding exceptions you don't want to have::

    python exceptional -f logfile.txt -e ValueError,AttributeError

Would exclude any ``ValueError`` or ``AttributeError`` from the list.

The tool can also read the log file from stdout, e.g.:

    cat logfile.txt | python exceptional

or 

    cat logfile.txt | python exceptional -e ValueError

This is based on [a script](https://gist.github.com/originell/1923003) by [@
originell](https://github.com/originell).