"""All processing functions for rendering views"""

from datetime import date
from calendar import weekday
from AltviaDogs.models import Dog
from AltviaDogs.models import Owner
from AltviaDogs.models import DogDay
from AltviaDogs import models

list_of_weekday_values = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}


def find_weekday_from_calendar(year, month, day):
    """take in date and find if weekday or weekend, return True for weekday"""
    return weekday(year, month, day)


def move_date_if_wknd(date, day_val):
    if day_val == 5:
        return date + 2
    elif day_val == 6:
        return date + 1
    else:
        return date

def determine_correct_date(date_value):
    year = date_value.year
    month = date_value.month
    day = date_value.day
    day_val = find_weekday_from_calendar(year, month, day)
    newday = move_date_if_wknd(day, day_val)
    date_value = date(year, month, newday)
    return date_value


def grab_list_of_dogs(date_value):
    # selected_date = determine_correct_date(date_value)
    # existence = verify_day_exists(selected_date)
    # if existence = True:
    dog_day = DogDay.objects.get(date_of_record__exact=date_value)
    # else:
    # dog_day = create_dog_day(date_value)
    available_dogs = dog_day.dogs.all()
    dog_list = ', '.join(d.name for d in available_dogs)
    return dog_list
