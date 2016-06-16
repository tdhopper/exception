
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import six

"""
test_exception
----------------------------------

Tests for `exception` module.
"""
import pytest

from mock import Mock

from exception import exception


@pytest.fixture
def simple_traceback():
    return """Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero"""


@pytest.fixture
def simple_traceback_buffer():
    return six.StringIO("""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero""")


def test_trivial(simple_traceback):
    exception.fileinput = Mock()
    exception.fileinput.filename = lambda: "X"

    errors = exception.extract_errors(simple_traceback.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]


    trace2 = "a\n{}\na\n\n\n".format(simple_traceback)

    errors = exception.extract_errors(trace2.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]


def test_file(simple_traceback, simple_traceback_buffer):
    errors = exception.extract_errors(simple_traceback_buffer.readlines())
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback) == out[0]


def test_deduplicate(simple_traceback):
    exception.fileinput = Mock()
    exception.fileinput.filename = lambda: "X"

    traceback = "{}\n{}".format(simple_traceback, simple_traceback)

    errors = exception.extract_errors(traceback.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]

