"""
Bite 268. Number Transformers

Input: an integer number, the target number
Output: the minimum number of operations required to reach to n from 1.

Two operations rules:
1.  multiply by 2
2.  int. divide by 3

The base number is 1. Meaning the operation will always start with 1
These rules can be run in any order, and can be run independently.
"""
from collections import deque


def num_ops(n):
    q = deque([(1, 0)])
    seen = set()

    while q:
        res, ops = q.popleft()
        if res == n:
            return ops
        if res // 3 not in seen:
            q.append((res // 3, ops + 1))
            seen.add(res // 3)
        if res * 2 not in seen:
            q.append((res * 2, ops + 1))
            seen.add(res * 2)



if __name__ == '__main__':
    test10 = num_ops(10) #6
    test12 = num_ops(12) #9
    test15 = num_ops(15) #17
    test33 = num_ops(33) #18
    test55 = num_ops(55) #24
