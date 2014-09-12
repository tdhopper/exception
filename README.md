Extract unique Python-Exceptions with their traceback from a log file.

## Installational

 Clone this repository and install with

    python setup.py install

This adds a utility called `exceptional` or `exceptional.exe` to your path.

## Usage

To extract the Python tracebacks from a log called _logfile.txt_, run:

    $ exceptional logfile.txt

If you want to exclude certain exceptions, try:

    $ exceptional -f logfile.txt -e ValueError,AttributeError

This would exclude would exclude any ``ValueError`` or ``AttributeError`` tracebacks from the output.

The tool can also read the log file from stdout, e.g.:

    cat logfile.txt | exceptional

or

    cat logfile.txt | exceptional -e ValueError

## Attribution

This is based on [a script](https://gist.github.com/originell/1923003) by [@
originell](https://github.com/originell).