"""
Bite 284. Pascal triangle
A Pascal triangle is a triangular array of integers constructed with the following characteristics:

1. The first row consists of the number 1.

2. For each subsequent row, each element is the sum of the numbers directly above it, on either side.

Here is an example of the first 5 rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Exercise
Given an input N, return the Nth row of Pascal's triangle in a list.

Example for N = 5
# >>> pascal(N) [1, 4, 6, 4, 1]
"""

from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    n = N - 1
    line = [1]
    for k in range(0, n):
        line.append(line[k] * (n - k) // (k + 1))
    return line if n >= 0 else []
