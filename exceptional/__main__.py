from __future__ import print_function
from argparse import ArgumentParser
import fileinput

# SETTINGS
MAX_LINE_LENGTH = 400
DELIMETER_LENGTH = 40


def get_options():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', dest='file',
                      help='The file to extract exceptions from',
                      metavar='FILE',
                      nargs='+',
                      type=str)
    parser.add_argument('-e', '--exclude', dest='exclude_list',
                      help='Exclude certain exceptions from output.',
                      default="",
                      metavar='Exception,Exception,...')
    return parser.parse_args()


def extract_errors(options):
    buffer_on = False
    error = ''
    last_error = ''
    for line in fileinput.input(options.file):
        if is_first_line(line):
            buffer_on = True
            first_line = line
        if buffer_on:
            # Truncate lines longer than 400 characters.
            if len(line) > MAX_LINE_LENGTH:
                line = line[:MAX_LINE_LENGTH]+'...\n'
            error += line
            if line and is_last_line(line, first_line):
                buffer_on = False
                if exclude_error(error, last_error, options.exclude_list):
                    last_error = error
                    error = ''
                    continue
                else:
                    yield fileinput.filename(), error
                    last_error = error
                    error = ''


def is_first_line(line):
    return line.startswith("Traceback (most recent call last):")


def is_last_line(line, first_line):
    return (line != first_line) and not line.startswith(" ")


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


def print_error(error):
    print(error)
    print(DELIMETER_LENGTH * "-")


def main():
    options = get_options()
    for filename, error in extract_errors(options):
        print("### %s ###\n" % filename) # TODO: add a flag for this
        print_error(error)


if __name__ == "__main__":
    main()