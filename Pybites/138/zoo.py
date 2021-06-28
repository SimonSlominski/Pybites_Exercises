"""
Bite 138. OOP fun at the Zoo
Finish the Animal class below adding one or more class variables and a classmethod so that the following code:

dog = Animal('dog')
cat = Animal('cat')
fish = Animal('fish')
lion = Animal('lion')
mouse = Animal('mouse')
print(Animal.zoo())
... produces the following output:

10001. Dog
10002. Cat
10003. Fish
10004. Lion
10005. Mouse
Few things to note here:

The sequencing starts at 10000,
Each animal gets title cased,
An individual animal should print the sequence+name string as well, so best to implement the __str__ method on the class.
So making another animal at this point, the following should work:

horse = Animal('horse')
assert str(horse) == "10006. Horse"
As usual this is what the pytest code tests when you submit your code.
"""
import itertools

class Animal():
    _sequence = itertools.count(10001)
    _zoo = []

    def __init__(self, name):
        self.id = next(self._sequence)
        self.name = name
        self._zoo.append(self)

    def __str__(self):
        return f"{self.id}. {self.name.title()}"

    @classmethod
    def zoo(cls):
        return '\n'.join('{}'.format(animal) for animal in cls._zoo)


if __name__ == '__main__':
    dog = Animal('dog')
    cat = Animal('cat')
    fish = Animal('fish')
    lion = Animal('lion')
    mouse = Animal('mouse')
    print(Animal.zoo())
