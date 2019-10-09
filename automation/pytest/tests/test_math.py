# test_math
import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    difference = 1 - 1
    assert difference == 0

# 
# Decorator for parametrizing tuples into test parameters. This is an 
# example of data-driven testing
#
@pytest.mark.parametrize(
    "a, b, expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])

def test_multiplication(a, b, expected):
    assert a * b == expected

#
# Test for error raising and verifying that the error is correct
#
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
