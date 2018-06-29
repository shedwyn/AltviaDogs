"""All processing functions for rendering views."""

from datetime import date
from calendar import weekday
# from AltviaDogs.models import Dog
# from AltviaDogs.models import Owner
from AltviaDogs.models import DogDay

list_of_weekday_values = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
    3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}


def find_weekday_from_calendar(year, month, day):
    """
    Determine day of week using list_of_weekday_values.

    take in tuple from an instance of a date and find if weekday or weekend,
    return True for weekday
    """
    return weekday(year, month, day)


def move_date_if_wknd(date, day_val):
    """
    Change day portion of given date to ensure it lands on a weekday.

    take in day(date) and associated value from list_of_weekday_values,
    correct weekend date to Monday, return day(date)
    """
    if day_val == 5:
        return date + 2
    elif day_val == 6:
        return date + 1
    else:
        return date


def determine_correct_date(date_instance):
    """
    Correct date to exclude weekends.

    take in instance of date, parse day from instance and test/correct
    for weekend dates, reset and return date instance to new day
    """
    year = date_instance.year
    month = date_instance.month
    day = date_instance.day
    day_val = find_weekday_from_calendar(year, month, day)
    newday = move_date_if_wknd(day, day_val)
    date_instance = date(year, month, newday)
    return date_instance


def verify_day_exists(date_instance):
    """
    Test to see if a DogDay value exists for selected date.

    take in an instance of date and return boolean value
    """
    list_of_dates_available = DogDay.objects.date_of_record.all()
    if date_instance in list_of_dates_available:
        return True
    else:
        return False


def create_new_dog_day(date_instance):
    """Create new instance of a DogDay."""
    return True


def grab_list_of_dogs(date_instance):
    """
    Find and return list of dogs for a given date.

    take in date instance, get list of dogs in DogDay for that date, format
    into comma sep string, return string of dog names
    """
    # existence = verify_day_exists(selected_date)
    # if existence = True:
    dog_day = DogDay.objects.get(date_of_record__exact=date_instance)
    # else:
    # dog_day = create_dog_day(date_value)
    available_dogs = dog_day.dogs.all()
    dog_list = ', '.join(d.name for d in available_dogs)
    return dog_list
