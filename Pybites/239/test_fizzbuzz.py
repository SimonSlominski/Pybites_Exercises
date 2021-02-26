"""
Bite 239. Test FizzBuzz

Note this is a Test Bite and uses Python 3.7 and MutPy 0.6.1

In our second Test Bite you will write tests for FizzBuzz.
Refer to the "Code to Test" tab, then start to write your pytests. Have fun!
"""
import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize('num, expected', [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16)
])
def test_fizzbuzz(num, expected) -> None:
    assert fizzbuzz(num) == expected

def test_type_error_with_arg() -> None:
    with pytest.raises(TypeError):
        fizzbuzz('1')

def test_type_error_no_arg() -> None:
    with pytest.raises(TypeError):
        fizzbuzz()
