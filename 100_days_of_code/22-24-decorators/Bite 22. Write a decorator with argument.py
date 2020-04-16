"""
Bite 22. Write a decorator with argument

Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

- would return: <p><strong>I code with PyBites</strong></p>
"""

from functools import wraps


def make_html(element):
    def inner_function(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return f'<{element}>{fn(*args, **kwargs)}</{element}>'
        return wrapper
    return inner_function


@make_html('p')
@make_html('strong')
def get_text(text):
    return text

def main():
    print(get_text('PYTHON TRADER'))

if __name__ == '__main__':
    main()
