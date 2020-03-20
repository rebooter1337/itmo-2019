# -*- coding: utf-8 -*-

from cli import contains, ls 
from cli import mk, rm, since
import subprocess


def test_ls(ls_fixture):
    """ls tests."""
    assert ls(ls_fixture[0]) == ls_fixture[1]


def test_mk(mk_fixture):
    """mk tests."""
    assert mk(mk_fixture[0]) == mk_fixture[1]


def test_rm(rm_fixture):
    """rm tests."""
    assert rm(rm_fixture[0]) == rm_fixture[1]


def test_contains(contains_fixture):
    """contains tests."""
    assert contains(contains_fixture[0]) == contains_fixture[1]


def test_since(since_fixture):
    """since tests."""
    assert since(
        since_fixture[0],
        since_fixture[1],
    ) == since_fixture[2]


def test_integration(integration_fixture):
    """Integration tests."""
    command, parameter = integration_fixture
    format_str  = 'python students/rebooter1337/3/cli.py {0} {1}'
    command_str  = format_str .format(command, parameter)
    assert subprocess.call(command_str , shell=True) == 0
