# -*- coding: utf-8 -*-

import file


def test_checkname():
    """Test for Checkname function."""
    assert file.checkname('Артем', ' Волков') == 'Артем Волков'


def test_sum():
    """Test for my_sum function."""
    assert file.my_sum(1, 2) == 3
    assert file.my_sum(2, 4) == 6


def test_mult():
    """Test for my_mult function."""
    assert file.my_mult(2, 2) == 4
    assert file.my_mult(3, 3) == 9
    assert file.my_mult(8, 0) == 0
