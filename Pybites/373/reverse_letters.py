"""
Bite 373. Reverse only Letters
Given a string, reverse only the English letters (lowercase or uppercase) in the string, leaving all non-English letters and other characters (e.g. numbers) in their original position.

Example:

# >>> from  reverse_letters import reverse_letters
# >>> string = "ab-cd"
# >>> reverse_letters(string)
'dc-ba'
Example 2:

# >>> from  reverse_letters import reverse_letters
# >>> string = "ab5DEf"
# >>> reverse_letters(string)
'fE5Dba'
Example 3:

# >>> from  reverse_letters import reverse_letters
# >>> string = "a-bC-dEf-ghIj"
# >>> reverse_letters(string)
'j-Ih-gfE-dCba'
"""


def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    alpha_str = "".join([char for char in string if char.isalpha()])
    right = len(alpha_str) -1

    out = ""

    for left in string:
        if left.isalpha():
            out += alpha_str[right]
            right -= 1
        else:
            out += left

    return out
