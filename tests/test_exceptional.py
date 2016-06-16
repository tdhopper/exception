
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import six

"""
test_exception
----------------------------------

Tests for `exception` module.
"""

from mock import Mock

from exception import exception


def test_trivial():
    exception.fileinput = Mock()
    exception.fileinput.filename = lambda: "X"

    trace = """Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero"""

    errors = exception.extract_errors(trace.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(trace.split('\n')) == out[0]


    trace2 = "a\n{}\na\n\n\n".format(trace)

    errors = exception.extract_errors(trace2.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(trace.split('\n')) == out[0]

def test_file():
    trace = """Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero"""
    trace_file = six.StringIO(trace)
    errors = exception.extract_errors(trace_file.readlines())
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(trace) == out[0]