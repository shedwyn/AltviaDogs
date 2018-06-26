"""All processing functions for rendering views"""

from datetime import date
from calendar import weekday
from AltviaDogs.models import Dog
from AltviaDogs.models import Owner
from AltviaDogs.models import DogDay

list_of_weekday_values = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}


def find_weekday_from_calendar(year, month, day):
    """take in date and find if weekday or weekend, return True for weekday"""
    return weekday(year, month, day)


def move_date_to_monday(day, day_val):
    if day_val = 5:
        return day + 2
    elif day_val = 6:
        return day + 1
    else:
        return day


def determine_correct_date(date_value):
    if date = 'today':
        year = date.today().year
        month = date.today().month
        day = date.today().day
    else:
        year = '2018'
        month = '6'
        day = '22'
    weekday = determine_weekday(year, month, day)
    # need to find date and Days
    # then test for Sat or sun
    calendar.weekday(date.today().year, date.today().month, date.today().day)
    current_date = 'date corrected'
    return current_date


 def grab_list_of_dogs(date_value):
    date = select_and_test_date()
    # test to see if record exists for this date
    # if not - create date
    dogs = Dog.objects.filter(date)
    # probably need test for if no dogs then return 'no dogs'
    # create sort order within logic (assign dog 1, dog 2, dog 3 for layout?)
    return dogs
