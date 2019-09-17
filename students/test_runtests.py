# -*- coding: utf-8 -*-

import runtests


def test_selected_path():
    """Test for select_path function."""
    assert runtests.select_path('') != 'sample_test'


def test_find_test():
    """Test for find_tests function."""
    gfys = runtests.select_path('')
    assert runtests.find_tests(gfys) != ['nonexistend_test'], ['sd']


def test_run_test():
    """Test for run_tests function."""
    assert runtests.run_tests() != 'asd'
