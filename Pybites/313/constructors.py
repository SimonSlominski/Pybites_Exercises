"""
Bite 313. Alternative constructors

In this Bite your are provides with a Domain class and a DomainException custom exception class.
You will add some validation to the current constructor to check if a valid domain name is passed in.

Next you will add a __str__ special method to represent the object (basically the name attribute)
and you will write two classmethods to construct domains:
1. from a URL
2. from an email

Here you can see the code in action (also make sure you check out the tests):
# >>> from constructors import Domain
# >>> str(Domain('google.com'))
# 'google.com'
# >>> str(Domain.parse_url("http://pybit.es"))
# 'pybit.es'
# >>> domain = Domain.parse_email("julian@pybit.es")
# >>> type(domain)
# <class 'constructors.Domain'>
# >>> str(domain)
'pybit.es'
"""

from urllib.parse import urlparse
import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        self.name = self._is_valid_name(name)

    def _is_valid_name(self, name):
        regex = r".*\.[a-z]{2,3}$"
        if not re.match(regex, name):
            raise DomainException
        return name

    # -----> Second approach to validate Class Attributes <-----
    # def __init__(self, name):
    #     # self.name = name
    #
    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     if re.match(r".*\.[a-z]{2,3}$", value):
    #         self.__name = value
    #     else:
    #         raise DomainException

    # -----> Third approach to validate Class Attributes <-----
    # def __init__(self, name):
    #     if not re.match(r'.*\.[a-z]{2,3}$', name.lower()):
    #         raise DomainException(f"{name} is an invalid domain")
    #     self.name = name

    @classmethod
    def parse_url(cls, url):
        return cls(urlparse(url).netloc)

    @classmethod
    def parse_email(cls, email):
        return cls(email.split('@')[1])

    def __str__(self):
        return self.name
