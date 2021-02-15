"""
Bite 167. Complete a User class: properties and representation dunder methods

Like last Bite you are asked to complete it, see the TODOs in the code below:

Complete the get_full_name property (more on properties here) that prints first and last name separated by a space.
Complete the username property following its docstring.
Complete the special representation dunder methods: __str__ and __repr__. Look at the tests what they should return.

Brace yourself for some bonus learning for a twist we added in __repr__ (but as it's a Beginner Bite we give you a hint!)
Apart from Ned's awesome answer on SO, to give you an idea about the difference between __str__ and __repr__,
check out how datetime implements them:

# >>> from datetime import datetime
# >>> dt = datetime.now()
# >>> str(dt)
'2019-02-04 23:05:27.376407'
# >>> repr(dt)
'datetime.datetime(2019, 2, 4, 23, 5, 27, 376407)'
"""

class User:
    """A User class
       (Django's User model inspired us)
    """

    def __init__(self, first_name, last_name):
        """Constructor, base values"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        """Return first separated by a whitespace
           and using title case for both.
        """
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def username(self):
        """A username consists of the first char of
           the user's first_name and the first 7 chars
           of the user's last_name, both lowercased.

           If this is your first property, check out:
           https://pybit.es/property-decorator.html
        """
        return f'{(self.first_name[0].lower() + self.last_name[:7]).lower()}'

    def __str__(self):
        return f'{self.get_full_name} ({self.username})'

    def __repr__(self):
        """Don't hardcode the class name, hint: use a
           special attribute of self.__class__ ...
        """
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}")'
