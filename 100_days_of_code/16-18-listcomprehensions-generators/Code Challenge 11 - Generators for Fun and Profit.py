"""
Code Challenge 11 - Generators for Fun and Profit

Inspired by David Beazley's Generator Tricks for Systems Programmers we ask you to turn the following unix pipeline
into Python code using generators. To get a bunch of .py files you can use our challenges repo you cloned. Or use a project of your own.

Note that in our experience one subprocess is not necessarily one generator, for example 'sort|uniq|sort'
can be easily combined into one, as well as 'grep|sed'. See our template if you need guidance.
"""

"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

from collections import Counter
from glob import glob
import re


def gen_files(pat):
    yield from glob(pat)

def gen_lines(files):
    for filename in files:
        with open(filename) as f:
            yield from f

def gen_grep(lines, pattern):
    regex = re.compile(pattern)
    for line in lines:
        if regex.match(line):
            yield regex.sub("", line).strip()

def gen_count(lines):
    yield from Counter(lines).most_common()


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    imports = gen_grep(lines, "import")
    result = gen_count(imports)

    for k, v in result:
        print(v, k)

