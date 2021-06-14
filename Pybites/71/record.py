"""
Bite 71. Keep state in a class + make its instance callable

In this Bite you write a small class to keep track of the max score in a game.
When called as a function it receives a new score and returns the max score.
Note it should work with negative numbers as well.

# >>> from record import RecordScore

#   >>> record = RecordScore()
#   >>> print(record(10))
#   10
#   >>> print(record(9))
#   10
#   >>> print(record(11))  # new max
#   11

#   >>> record = RecordScore()
#   >>> print(record(-5))
#   -5
#   >>> print(record(-10))
#   -5
#   >>> print(record(-2))  # new max
#   -2

Use the __call__ dunder ("special") method to make the RecordScore class callable.
"""

class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.record = float('-inf')

    def __call__(self, num):
        self.record = max(self.record, num)
        return self.record
