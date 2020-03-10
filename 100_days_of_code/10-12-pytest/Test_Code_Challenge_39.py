from Code_Challenge_39 import is_even, sum
import pytest


def test_is_even():
	assert is_even(2)


# def test_sum():
# 	assert sum(1, 2) == 4


@pytest.mark.parametrize('num1, num2, expected', [(3,5,8)])
def test_sum(num1, num2, expected):
	assert sum(num1, num2) == expected

