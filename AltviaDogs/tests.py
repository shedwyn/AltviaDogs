"""All Unit Tests for Views and Logic."""

from datetime import date
from calendar import weekday
from datetime import timedelta
# from calendar import weekday
# from django.test import TestCase

# Create your tests here.


def move_date_if_weekend(date_val, day_val):
    if day_val == 5:
        return date_val + timedelta(days=2)
    elif day_val == 6:
        return date_val + timedelta(days=1)
    else:
        return date_val


def determine_correct_date(date_val):
    day_val = weekday(date_val.year, date_val.month, date_val.day)
    correct_date = move_date_if_weekend(date_val, day_val)
    return correct_date


def test_saturday_value_is_5():
    date_val = date(2018, 7, 14)
    assert weekday(date_val.year, date_val.month, date_val.day) == 5


def test_advance_date_2_days_when_given_5():
    date_val = date(2018, 7, 14)
    assert date(2018, 7, 16) == move_date_if_weekend(date_val, 5)


def test_advance_date_1_day_when_given_6():
    date_val = date(2018, 7, 15)
    assert date(2018, 7, 16) == move_date_if_weekend(date_val, 6)


def test_finds_weekday_value():
    date_val = date(2018, 7, 14)
    weekday_val = weekday(date_val.year, date_val.month, date_val.day)
    assert determine_correct_date(date_val) == weekday_val

