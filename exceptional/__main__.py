from __future__ import print_function
from optparse import OptionParser
import fileinput

MAX_LINE_LENGTH = 400
DELIMETER_LENGTH = 80

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
    error = ''
    last_error = ''
    for line in fileinput.input(options.file):
        first_line = line.startswith("Traceback (most recent call last):")
        if first_line:
            bufMode = True
        if bufMode:
            # Truncate lines longer than 400 characters.
            if len(line) > MAX_LINE_LENGTH:
                line = line[:MAX_LINE_LENGTH]+'...\n'
            error += line
            if line and is_last_line(line, first_line):
                bufMode = False
                if exclude_error(error, last_error, options.exclude_list):
                    last_error = error
                    continue
                else:
                    print(error)
                    print(DELIMETER_LENGTH * "-")
                    last_error = error


def is_last_line(line, first_line):
    return not first_line and not line.startswith(" ")


def exclude_error(error, last_error, exclude_list):
    excludes = exclude_list.split(',') if exclude_list else []
    if any([excl in error for excl in excludes]):
        return True
    elif error.strip() == "":
        return True
    elif error == last_error:
        return True
    else:
        return False


def main():
    options, args = get_options()
    extract_errors(options)


if __name__ == "__main__":
    main()