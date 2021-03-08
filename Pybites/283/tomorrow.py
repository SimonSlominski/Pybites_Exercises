"""
Bite 283. Like there's no tomorrow?
Ever have difficulty remembering what today's date is?

How about tomorrow's?

I know I do...  Help me out by completing the tomorrow() function to return a date object with tomorrow's date.
"""
import datetime


def tomorrow(today=None):
    if not today:
        today = datetime.date.today()
    return today + datetime.timedelta(days=1)
