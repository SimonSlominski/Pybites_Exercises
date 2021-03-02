"""
Bite 172. Having fun with Python Partials

Meet another gem in the standard library: functools, which contains tools for functional-style programming.

In this Bite you will play with its useful partial() function which - as per PEP 309 -
lets you construct variants of existing functions that have some of the parameters filled in.

In this Bite you will apply this concept to the round builtin:

# >>> round(10.42342, 2)
10.42

Write two partials to add the default behavior of rounding to 0 and 4 places respectively.
"""

from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int =  partial(round, ndigits=0)
rounder_detailed =  partial(round, ndigits=4)
