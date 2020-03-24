"""
Bite 3. Word Values

Calculate the dictionary word that would have the most value in Scrabble.

There are 3 tasks to complete for this Bite:

First write a function to read in the dictionary.txt file (= DICTIONARY constant),
returning a list of words (note that the words are separated by new lines).

Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES.
Letters that are not in LETTER_SCORES should be omitted (= get a 0 score).

With these two pieces in place, write a third function that takes a list of words and returns the word with the highest value.
"""

import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as file:
        words = [line.strip("\n") for line in file]
    return words


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    # return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)
    word_score = 0

    for char in word.upper():
        if char in LETTER_SCORES:
            word_score += LETTER_SCORES.get(char, 0)

    return word_score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    # return max(words, key=calc_word_value)
    top_score = 0
    top_word = ''

    for word in words:
        if calc_word_value(word) > top_score:
            top_score = calc_word_value(word)
            top_word = word

    return top_word
