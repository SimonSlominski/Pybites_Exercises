"""
Can you write a simple list comprehension to convert these names to title case
(brad pitt -> Brad Pitt). Or reverse the first and last name?

Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:

pairs = gen_pairs()
for _ in range(10):
    next(pairs)

Should print (values might change as random):

Arnold teams up with Brad
Alec teams up with Julian

Have fun!
"""
import random
import itertools


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# list comprehension to title case names
titled_names = [name.title() for name in NAMES]


# list comprehension to reverse first and last names
def reverse_first_last_names(name):
    first, last = name.split()
    return f'{last} {first}'


def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]

    while True:
        first, second = None, None
        while first == second:
            first, second = random.sample(first_names, 2)

        yield f'{first} teams up with {second}'

pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))

first_ten = itertools.islice(pairs, 10)
print(list(first_ten))
