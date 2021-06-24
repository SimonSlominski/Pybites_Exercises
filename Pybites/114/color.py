"""
Bite 114. Implement a Color class with staticmethod

Your task will be to implement the following:

1) add self.rgb to the __init__ method that gets its value from the provided COLOR_NAMES dictionary
(k, v = color_name, rgb tuple = e.g.: "ALICEBLUE": (240, 248, 255)). If the value does not exist, just assume it is None.
2) Convert hex2rgb and rgb2hex into @staticmethods.
3) Validate the values being passed to each of these staticmethods and raise a ValueError if called with bad data.
4) Add a __repr__ method whose value is in the form of Color('white'), with white being the inital value that it was initialized with.
5) Add a __str__ method whose value is the RGB value of the color if it is found in COLOR_NAMES, else return Unknown.
"""

import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402
print(COLOR_NAMES)

class Color:
    """
    Color class. Takes the string of a color name and returns its RGB value.
    """
    def __init__(self, color):
        self.color = color.upper()
        try:
            self.rgb = COLOR_NAMES[self.color]
        except KeyError:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        hex_color = hex.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if int(rgb[0]) > 255 or int(rgb[1]) > 255 or int(rgb[2]) > 255:
            raise ValueError
        if int(rgb[0]) < 0 or int(rgb[1]) < 0 or int(rgb[2]) < 0:
            raise ValueError
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{str(self.__class__.__name__)}('{self.color.lower()}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            message = 'Unknown'
        else:
            message = str(self.rgb)
        return message
