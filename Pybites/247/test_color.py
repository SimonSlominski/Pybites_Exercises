"""
Bite 247. Mocking a standard library function

Note this is a Test Bite and uses Python 3.7 and MutPy 0.6.1

In this Bite you will mock out a function of the standard library, more specifically random.sample.

We wrote a small generator that produces hex colors.
We also provided a fixture to initialize the generator so you can just call next(gen) to get the next hex value.

Use unittest.mock's patch to mock out the call to sample.
It might be a bit tricky, but once you get this one down you possess a valuable testing skill!

Have fun and keep calm and test with pytest!
"""

from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@patch.object(color, "sample", side_effect=[
    [255, 0, 0],    # red
    [0, 255, 0],    # green
    [0, 0, 255],    # blue
    [255, 255, 0],  # yellow
])
def test_gen_hex_color(mock, gen):
    assert next(gen) == "#FF0000"
    assert next(gen) == "#00FF00"
    assert next(gen) == "#0000FF"
    assert next(gen) == "#FFFF00"
