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

def main():
    parser = OptionParser()
    parser.add_option('-f', '--file', dest='file',
                      help='The file to extract exceptions from',
                      default="-",
                      metavar='FILE')
    parser.add_option('-e', '--exclude', dest='exclude_list',
                      help='Exclude certain exceptions from output.',
                      default="",
                      metavar='Exception,Exception,...')
    options, args = parser.parse_args()

    def is_last_line(line, first_line):
        return not first_line and not line.startswith(" ")


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


    unique_errs = set(errors)
    excludes = []
    if options.exclude_list:
        excludes = options.exclude_list.split(',')

    for err in unique_errs:
        if any([excl in err for excl in excludes]):
            continue
        if err.strip() == "":
            continue
        print err
        print "---"

if __name__ == "__main__":
    main()