import math_complicated


def test_add():
    assert math_complicated.add(1, 2) == 3


def test_add_zeros():
    assert math_complicated.add(0, 0) == 0
