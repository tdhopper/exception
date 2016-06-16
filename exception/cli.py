# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import fileinput

from argparse import ArgumentParser

from .exception import extract_errors, print_error


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


def main():
    options = get_options()
    for filename, error in extract_errors(fileinput.input(options.file),
                                          options.exclude_list):
        print("### %s ###\n" % filename)  # TODO: add a flag for this
        print_error(error)


if __name__ == "__main__":
    main()
