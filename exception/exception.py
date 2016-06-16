# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import fileinput

from argparse import ArgumentParser

# SETTINGS
MAX_LINE_LENGTH = 400
DELIMETER_LENGTH = 40


def extract_errors(line_generator, exclude_list=None):
    buffer_on = False
    error = ''
    last_error = ''
    for line in line_generator:
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
                if exclude_error(error, last_error, exclude_list):
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

