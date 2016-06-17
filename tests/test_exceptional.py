
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import six
import os

"""
test_exception
----------------------------------

Tests for `exception` module.
"""
import pytest

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


@pytest.fixture
def mock_filename(mocker):
    mocker.patch('fileinput.filename', spec=True)
    exception.fileinput.filename.return_value = "X"


def test_trivial(mock_filename, simple_traceback):
    """Check that a simple example is fine"""
    errors = exception.extract_errors(simple_traceback.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]

    # Add some trash before and afterthe
    trace2 = "a\n{}\na\n\n\n".format(simple_traceback)

    errors = list(exception.extract_errors(trace2.split("\n")))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]

    assert errors[0][0] == "X"


def test_file(mock_filename, simple_traceback, simple_traceback_buffer):
    """Correctly parses an input buffer"""
    errors = exception.extract_errors(simple_traceback_buffer.readlines())
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback) == out[0]


def test_multiple_exceptions(mock_filename, simple_traceback):
    """Extract two exceptions from a string"""
    trace1 = simple_traceback
    trace2 = simple_traceback.replace("ZeroDivisionError", "ValueError")

    traceback = "{}\n{}".format(trace1, trace2)
    errors = exception.extract_errors(traceback.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 2
    assert "".join(trace1.split('\n')) == out[0]
    assert "".join(trace2.split('\n')) == out[1]


def test_deduplicate(mock_filename, simple_traceback):
    """Duplicate exceptions in sequence are ignored"""
    traceback = "{}\n{}".format(simple_traceback, simple_traceback)

    errors = exception.extract_errors(traceback.split("\n"))
    out = [error for filename, error in errors]
    assert len(out) == 1
    assert "".join(simple_traceback.split('\n')) == out[0]


@pytest.mark.skipif(os.environ.get('TRAVIS'), reason="Can't get path to work on Travis")
def test_cli():
    from subprocess import check_output
    import os
    root = os.path.dirname(__file__)
    result = check_output(["exception", "-f", "{}/fixtures/real_log.log".format(root)])

    true = """### {}/fixtures/real_log.log ###

Traceback (most recent call last):
  File "local/lib/python2.7/site-packages/pykafka/cluster.py", line 242, in _request_metadata
    ssl_config=self._ssl_config)
  File "local/lib/python2.7/site-packages/pykafka/broker.py", line 97, in __init__
    self.connect()
  File "local/lib/python2.7/site-packages/pykafka/broker.py", line 211, in connect
    self._connection.connect(self._socket_timeout_ms)
  File "local/lib/python2.7/site-packages/pykafka/connection.py", line 169, in connect
    (self.source_host, self.source_port)
  File "/usr/lib/python2.7/socket.py", line 571, in create_connection
    raise err
error: [Errno 111] Connection refused

----------------------------------------
""".format(root)
    assert result == true
