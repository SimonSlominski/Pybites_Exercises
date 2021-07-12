"""
Bite 199. Multiple inheritance (__mro__)

Implement the following class structure: print(Child.__mro__):
(<class '__main__.Child'>,
 <class '__main__.Father'>,
 <class '__main__.Mother'>,
 <class '__main__.Person'>,
 <class 'object'>)

Each class has the following string representation:
person = Person()
dad = Father()
mom = Mother()
child = Child()

print(person)
print(dad)
print(mom)
print(child)

Output:
I am a person
I am a person and cool daddy
I am a person and awesome mom
I am the coolest kid
You should use inheritance here, so the I am a person substring should only occur in the Person base class.
"""


class Person():
    def __str__(self):
        return 'I am a person'


class Father(Person):
    def __str__(self):
        return f'{super().__str__()} and cool daddy'


class Mother(Person):
    def __str__(self):
        return f'{super().__str__()} and awesome mom'


class Child(Father, Mother):
    def __str__(self):
        return 'I am the coolest kid'
