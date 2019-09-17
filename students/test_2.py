# -*- coding: utf-8 -*-

import file


def test_div():
    """Test for my_div function."""
    assert file.my_div(1, 1) == 1
    assert isinstance(file.my_div(1, 1), float)
    assert file.my_div(6, 2) == 3
    assert file.my_div(8, 4) == 2
