# -*- coding: utf-8 -*-

import subprocess  # noqa: S404
from cli import contains, ls  # noqa I001
from cli import mk, rm, since  # noqa I001


def test_ls(ls_fixture):
    """Ls tests."""
    assert ls(ls_fixture[0]) == ls_fixture[1]


def test_mk(mk_fixture):
    """Mk tests."""
    assert mk(mk_fixture[0]) == mk_fixture[1]


def test_rm(rm_fixture):
    """Rm tests."""
    assert rm(rm_fixture[0]) == rm_fixture[1]


def test_contains(contains_fixture):
    """Contains tests."""
    assert contains(contains_fixture[0]) == contains_fixture[1]


def test_since(since_fixture):
    """Since tests."""
    assert since(
        since_fixture[0],
        since_fixture[1],
    ) == since_fixture[2]


def test_integration(integration_fixture):
    """Integration tests."""
    command, parameter = integration_fixture
    format_str = 'python students/rebooter1337/3/cli.py {0} {1}'
    command_str = format_str .format(command, parameter)
    assert subprocess.call(command_str, shell=True) == 0  # noqa: S602
