"""
Bite 181. Keep a list sorted upon insert

Complete the add method of the OrderedList class which takes a num argument
and adds that to the self._numbers list keeping it ordered upon insert.

Using a manual .sort() or .sorted() each time is not allowed. Look into the bisect module how to do it ...

Here is how it should works:

order = OrderedList()
order.add(10)
print(order)  # __str__ already provided
order.add(1)
print(order)
order.add(16)
print(order)
order.add(5)
print(order)
Output:

10
1, 10
1, 10, 16
1, 5, 10, 16
"""

from bisect import insort


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        return insort(self._numbers, num)
        pass

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)
