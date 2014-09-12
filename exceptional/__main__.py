"""
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
"""
from optparse import OptionParser
import fileinput


def get_options():
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='file',
                      help='The file to extract exceptions from',
                      default="-",
                      metavar='FILE')
    parser.add_option('-e', '--exclude', dest='exclude_list',
                      help='Exclude certain exceptions from output.',
                      default="",
                      metavar='Exception,Exception,...')
    return parser.parse_args()


def extract_errors(options):
    bufMode = False
    buf = ''
    errors = []
    for line in fileinput.input(options.file):
        first_line = line.startswith("Traceback (most recent call last):")
        if first_line:
            bufMode = True
        if bufMode:
            # Truncate lines longer than 400 characters.
            if len(line) > 400:
                line = line[:400]+'...\n'
            buf += line
        if bufMode and line and is_last_line(line, first_line):
            errors.append(buf)
            buf = ''
            bufMode = False
    return errors


def is_last_line(line, first_line):
    return not first_line and not line.startswith(" ")


def exclude_errors(errors, exclude_list):
    new_errors = []
    excludes = exclude_list.split(',') if exclude_list else []
    for err in errors:
        if any([excl in err for excl in excludes]):
            continue
        if err.strip() == "":
            continue
        new_errors.append(err)
    return new_errors


def print_errors(errors):
    for err in errors:
        print err
        print "---"


def main():
    options, args = get_options()

    errors = extract_errors(options)
    errors = set(errors) # TODO: Add flag for this
    errors = exclude_errors(errors, options.exclude_list)
    print_errors(errors)


if __name__ == "__main__":
    main()