"""
Bite 18. Find the most common word

Write a function that returns the most common (non stop)word in this Harry Potter text.

Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords.
Your function should return a tuple of (most_common_word, frequency).

The template code already loads the Harry Potter text and list of stopwords in.

Check the tests for more info - have fun!
"""

import os
import re
import urllib.request

from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    with open(harry_text) as file:
        text = file.read()

    text = text.lower()
    text = re.sub("[^a-z ']+", " ", text).split()

    with open(stopwords_file) as file:
        stopwords = file.read().split()

    words = [word for word in text if word not in stopwords]

    words_counter = Counter(words)
    return words_counter.most_common(1)[0]


# Pybites solution
# def get_harry_most_common_word():
#     with open(stopwords_file) as f:
#         stopwords = set(f.read().strip().lower().split('\n'))
#
#     with open(harry_text) as f:
#         words = [re.sub(r'\W+', r'', word)  # [^a-zA-Z0-9_]
#                  for word in f.read().lower().split()]
#
#         words = [word for word in words if word.strip()
#                  and word not in stopwords]
#
#         cnt = Counter(words)
#         return cnt.most_common(1)[0]
