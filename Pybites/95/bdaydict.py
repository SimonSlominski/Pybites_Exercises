"""
Bite 95. Subclass the dict built-in
In this Bite you will subclass the dict built-in to support a birthday dictionary.

This dictionary takes names as keys and birthday dates as values.
Implement the __setitem__ dunder method to print a message every time somebody gets added with a birthday
that is already in the dictionary. It should work like this when running it in the REPL:

  # >>> from datetime import date
  # >>> from bdaydict import BirthdayDict
  # >>> bd = BirthdayDict()
  # >>> bd['bob'] = date(1987, 6, 15)
  # >>> bd['tim'] = date(1984, 7, 15)
  # >>> bd['mary'] = date(1987, 6, 15)  # whole date match
  # Hey mary, there are more people with your birthday!
  # >>> bd['sara'] = date(1987, 6, 14)
  # >>> bd['mike'] = date(1981, 7, 15)  # day + month match
  Hey mike, there are more people with your birthday!

So if day and month are the same, you have a match, the year can be different.
Use MSG to print the message, string replacing it with the name key of the newly added person.
"""
from datetime import date


MSG = 'Hey {}, there are more people with your birthday!'

class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        for dt in self.values():
            if birthday.strftime("%d%m") == dt.strftime("%d%m"):
                print(MSG.format(name))
        super().__setitem__(name, birthday)
        # dict.__setitem__(self, name, birthday) <- it also works


if __name__ == "__main__":
    bd = BirthdayDict()
    bd['bob'] = date(1987, 6, 15)
    bd['tim'] = date(1984, 7, 15)
    bd['vim'] = date(1984, 7, 15)
