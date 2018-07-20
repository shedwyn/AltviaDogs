"""All Unit Tests for Views and Logic."""

from datetime import date
from calendar import weekday
from datetime import timedelta
# from calendar import weekday
# from django.test import TestCase

# Create your tests here.


def move_date_if_weekend(date_val, weekday_val):
    if weekday_val == 5:
        return date_val + timedelta(days=2)
    elif weekday_val == 6:
        return date_val + timedelta(days=1)
    else:
        return date_val

def find_weekday_value(date_val):
    return weekday(date_val.year, date_val.month, date_val.day)


def determine_correct_date(date_val):
    weekday_val = find_weekday_value(date_val)
    correct_date = move_date_if_weekend(date_val, weekday_val)
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
    assert weekday_val == find_weekday_value(date_val)


def test_determine_correct_date_given_a_Saturday():
    date_val = date(2018,7,14)
    correct_date = date(2018, 7, 16)
    assert correct_date == determine_correct_date(date_val)

def test_determine_correct_date_given_a_Sunday():
    date_val = date(2018, 7, 15)
    correct_date = date(2018, 7, 16)
    assert correct_date == determine_correct_date(date_val)


def test_determine_correct_date_given_a_Friday():
    date_val = date(2018, 7, 20)
    correct_date = date_val
    assert correct_date == determine_correct_date(date_val)



