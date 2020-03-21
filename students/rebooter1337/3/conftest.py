# -*- coding: utf-8 -*-

import pytest
import os


DIR = 'directory'
TEST_FILE = 'test.py'
DATE_TIME = '2020-01-14_04:20:00'


@pytest.fixture(params=[
    ('empty', [], []),
    ('dirs', [DIR], [DIR]),
    ('files', [TEST_FILE], [TEST_FILE]),
    ('dirs_and_files', [DIR, TEST_FILE], [DIR, TEST_FILE]),
])
def ls_fixture(tmp_path, request):
    """Ls fixture."""
    rule = request.param[0]
    path = tmp_path / rule
    path.mkdir()
    for name in request.param[1]:
        folder_item = path / name
        folder_item.join() if '.' in request.param[1] else folder_item.mkdir()
    yield (path, request.param[2])


@pytest.fixture(params=[
    (TEST_FILE, 'Success'),
    ('блабла.py', 'Success'),
    ('conftest1.py', 'Error'),
    ('&unable/.py', 'Error'),
])
def mk_fixture(request):
    """Mk fixture."""
    rule = request.param[0]
    if rule == 'conftest1.py':
        open(rule, 'w+').close()  # noqa WPS515
    yield request.param
    if os.path.isfile(rule):
        os.remove(rule)


@pytest.fixture(params=[
    (TEST_FILE, 'Success'),
    (DIR, 'Error'),
    ('&unable/.py', 'Error'),
])
def rm_fixture(tmp_path, request):
    """Rm fixture."""
    rule = request.param[0]
    if '.' in rule:
        try:
            open(rule, 'w+').close()  # noqa WPS515
        except FileNotFoundError:
            pass  # noqa WPS420
    else:
        new_item = tmp_path / rule
        new_item.mkdir()
    yield request.param


@pytest.fixture(params=[
    ('conftest2.py', True),
    ('&unable/.py', False),
    (DIR, False),
])
def contains_fixture(tmp_path, request):
    """Contains fixture."""
    rule = request.param[0]
    if '.' not in rule:
        new_item = tmp_path / rule
        new_item.mkdir()
    elif rule == 'conftest2.py':
        my_file = open(rule, 'w+')
        my_file.close()
    yield request.param
    if os.path.isfile(rule):
        os.remove(rule)


@pytest.fixture(params=[
    ('empty', DATE_TIME, [], []),
    ('dirs', DATE_TIME, [DIR], [DIR]),
    ('files', DATE_TIME, [TEST_FILE], [TEST_FILE]),
    ('dirs_and_files', DATE_TIME, [DIR, TEST_FILE], [DIR, TEST_FILE]),
    ('wrongDate', '2020-1204-04:20:00', [TEST_FILE], 'Use mask: y-m-d-h:m:s'),
])
def since_fixture(tmp_path, request):
    """Since fixture."""
    rule = request.param[0]
    path = tmp_path / rule
    path.mkdir()
    for name in request.param[2]:
        folder_item = path / name
        if '.' in request.param[2]:
            folder_item.join()
        else:
            folder_item.mkdir()
    yield (request.param[1], path, request.param[3])


@pytest.fixture(params=[
    ('ls', ''),
    ('mk', TEST_FILE),
    ('contains', TEST_FILE),
    ('rm', TEST_FILE),
])
def integration_fixture(request):
    """Integration fixture."""
    yield request.param
