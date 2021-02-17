"""
Bite 47. Write a new password field validator

You know these Create a new password forms? They do a lot of checks to make sure
you make a password that is hard to guess and you will surely forget.

In this Bite you will write a validator for such a form field.

Complete the validate_password function below. It takes a password str and validates that it:

is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
If the password matches all criteria the function should store the password in used_passwords and return True.
"""

import string

LOWERCASE_CHARS = string.ascii_lowercase
UPPERCASE_CHARS = string.ascii_uppercase
PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    pass_len = 6 <= len(password) <= 12
    num_of_digit = sum(1 for c in password if c.isdigit()) >=1
    num_of_lcase = sum(1 for c in password if c in LOWERCASE_CHARS) >=2
    num_of_ucase = sum(1 for c in password if c in UPPERCASE_CHARS) >=1
    num_of_punct = sum(1 for c in password if c in PUNCTUATION_CHARS) >=1
    pass_not_used = password not in used_passwords

    password_validations = [pass_len,
                            num_of_digit,
                            num_of_lcase,
                            num_of_ucase,
                            num_of_punct,
                            pass_not_used]

    if False in password_validations:
        return False
    else:
        used_passwords.add(password)
    return True
