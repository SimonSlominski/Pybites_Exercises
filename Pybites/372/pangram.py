"""
Bite 372. Validate Pangram
A pangram, according to the Oxford English Dictionary, is a sentence or verse that contains all of the letters of the alphabet.

Given a string containing only English letters, write a function that returns True if sentence is a pangram or False otherwise.

Make sure to remove any whitespace and lowercase the string.

Example:

# >>> from  pangram import validate_pangram
# >>> sentence = "The quick brown fox jumps over a lazy dog"
# >>> validate_pangram(sentence)
True
Example 2:

# >>> from  pangram import validate_pangram
# >>> sentence = "PYBITES IS A COMMUNITY OF PYTHON CODERS"
# >>> validate_pangram(sentence)
False
"""


import string


def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower().replace(" ", ""))
    return alphabet_set == sentence_set



if __name__ == "__main__":
    sentence_a = "thequickbrownfoxjumpsoverthelazydog"
    sentence_b = "The five boxing wizards jump quickly"
    validate_pangram(sentence_a)
    validate_pangram(sentence_b)
