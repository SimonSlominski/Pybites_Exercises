"""
Bite 154. Write your own Data Class

In this Bite we have you write a data class called Bite that managed 3 attributes: number, title, and level.
Their types are int, str and str respectively.

There are 3 more requirements:
1) title needs to be capitalized upon instantiation (you get a hint in the tests for this one :)
- make sure to read the tests for additonal specs, including some of the differences between data classes and namedtuples!)
2) level takes a default argument of Beginner.
3) A collection of Bite instances needs to be orderable (using sort / sorted - this is not by default but configurable ...)
"""

from dataclasses import dataclass


@dataclass(order=True)
class Bite:

    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        object.__setattr__(self, "title", self.title.capitalize())
