"""
Bite 135. Sort a list of book objects

In this Bite you are going to look at a list of Book namedtuples and sort them by various criteria.
Complete the 4 functions below.
Consider using lambda and/or one or more helper functions and/or attrgetter (operator module).
"""

from collections import namedtuple
from datetime import datetime
from operator import attrgetter

Book = namedtuple('Book', 'title authors pages published')

books = [
    Book(title="Python Interviews",
         authors="Michael Driscoll",
         pages=366,
         published="2018-02-28"),
    Book(title="Python Cookbook",
         authors="David Beazley, Brian K. Jones",
         pages=706,
         published="2013-05-10"),
    Book(title="The Quick Python Book",
         authors="Naomi Ceder",
         pages=362,
         published="2010-01-15"),
    Book(title="Fluent Python",
         authors="Luciano Ramalho",
         pages=792,
         published="2015-07-30"),
    Book(title="Automate the Boring Stuff with Python",
         authors="Al Sweigart",
         pages=504,
         published="2015-04-14"),
]


# all functions return books sorted in ascending order.

def sort_books_by_len_of_title(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted(books, key=lambda x: len(x[0]))

def sort_books_by_first_authors_last_name(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted(books, key=lambda x: x[1].split(" ")[1])

# def _get_first_authors_last_name(book):
#     return book.authors.split(',')[0].split()[-1]
#
#
# def sort_books_by_first_authors_last_name(books=books):
#     """
#     Expected last book in list:
#     Automate the Boring Stuff with Python
#     """
#     # 2. complex lambda -> helper function
#     return sorted(books, key=_get_first_authors_last_name)

def sort_books_by_number_of_page(books=books):
    """
    Expected last book in list:
    Fluent Python
    """
    return sorted(books, key=lambda x: x[2])

# def sort_books_by_number_of_page(books=books):
#     """
#     Expected last book in list:
#     Fluent Python
#     """
#     # 3. by attribute -> attrgetter
#     return sorted(books, key=attrgetter("pages"))

def sort_books_by_published_date(books=books):
    """
    Expected last book in list:
    Python Interviews
    """
    return sorted(books, key=lambda x: x[3])

# def _date_str_to_dt(book):
#     return datetime.strptime(book.published, '%Y-%m-%d')
#
# def sort_books_by_published_date(books=books):
#     """
#     Expected last book in list:
#     Python Interviews
#     """
#     # 2b. again more readable using a helper function
#     return sorted(books, key=_date_str_to_dt)
