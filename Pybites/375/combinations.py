"""
Bite 375. Find All Letter Combinations of a Phone Number

The typical phone keypad (pictured) features numbers (0 - 9),
letters mapped to some of those numbers (2 - 9, inclusive), and two non-numeric characters (* and #).

Now imagine it's the 1950s, you live in a small village with 900 other villagers,
any of whom you can reach simply by dialing the last four digits of their telephone number
(in other words, you only need to dial "5309" to reach Jenny, not "867-5309").

Given a string of up to four digits, return a list of strings where each string represents
a valid combination of letters that can be formed from the input.

Raise a ValueError if the input digits string contains non-digit characters or more than four digits.

Example 1:
# >>> from  combinations import generate_letter_combinations
# >>> digits =  "24"
# >>> generate_letter_combinations(digits)
['ag', 'ah', 'ai', 'bg', 'bh', 'bi', 'cg', 'ch', 'ci']

Example 2:
# >>> from  combinations import generate_letter_combinations
# >>> digits =  "232"
# >>> generate_letter_combinations(digits)
[
    "aaa", "aab",  "aac", "aba", "abb", "abc",
    "aca", "acb", "acc", "baa", "bab", "bac",
    "bba", "bbb", "bbc", "bca", "bcb", "bcc",
    "caa", "cab", "cac", "cba", "cbb", "cbc",
    "cca", "ccb", "ccc"
]
"""
from itertools import product


def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    keypad_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    if not digits.isdigit() or len(digits) > 4:
        raise ValueError("Non-digit characters or it has more than four digits")

    groups = [keypad_dict[number] for number in digits]

    return ["".join(letter) for letter in product(*groups)]




if __name__ == "__main__":
    print(generate_letter_combinations("2"))
    print(generate_letter_combinations("24"))
