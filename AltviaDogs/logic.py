"""All processing functions for rendering views.

All "grab" functions (grabbing entire usually grabbing object itself or query
set or bundle of objects for many to many field) are called from Views.py
and given a corrected date (weekday date object instance) by Views.py
"""

from datetime import date
from calendar import weekday
from AltviaDogs.models import Dog
# from AltviaDogs.models import Owner
from AltviaDogs.models import DogDay

list_of_weekday_values = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
    3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}
# ^ should this live within the class as a part of DogDay?


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
    if DogDay.objects.filter(date_of_record=date_instance).exists():
        return True
    else:
        return False


def create_new_dog_day(date_instance):
    """Create new instance of a DogDay."""
    new_dog_day = DogDay(date_of_record=date_instance)
    new_dog_day.save()
    return True


def remove_dog_from_dog_day(dog_day_id, single_dog):
    """Remove one dog object from selected DogDay."""
    curr_dog_day = DogDay.objects.get(id=dog_day_id)
    # curr_dog = Dog.objects.get(id=single_dog)
    curr_dog_day.dogs.remove(Dog.objects.get(id=single_dog))
    curr_dog_day.save()
    return True


def add_dog_to_dog_day(dog_day, single_dog):
    """Add one dog object to selected DogDay."""
    dog_day.dogs.remove(single_dog)
    dog_day.save()
    return True


def grab_date_for_dog_day(dog_day_id):
    """Return DogDay object's date."""
    dog_day = DogDay.objects.get(id=dog_day_id)
    return dog_day.date_of_record


def grab_correct_dog_day(date_instance):
    """Return correct DogDay Object based on date."""
    existence = verify_day_exists(date_instance)
    if existence is True:
        dog_day = DogDay.objects.get(date_of_record__exact=date_instance)
    else:
        create_new_dog_day(date_instance)
        dog_day = DogDay.objects.get(date_of_record__exact=date_instance)
    return dog_day


def grab_scheduled_dogs(date_instance):
    """
    Find and return group of dogs for a given date.

    take in date instance, get correct DogDay instance, pull all Dogs scheduled
    on that DogDay and return
    """
    dog_day = grab_correct_dog_day(date_instance)
    scheduled_dogs = dog_day.dogs.all().order_by('name')
    return scheduled_dogs


def grab_not_scheduled_dogs(date_instance):
    """
    Find and return group of dogs for a given date.

    take in date instance, get correct DogDay instance, pull all Dogs not
    scheduled on that DogDay and return
    """
    dog_day = grab_correct_dog_day(date_instance)
    available_dogs = dog_day.dogs.all().order_by('name')
    return available_dogs


def pull_correct_dog_name(dog_id):
    """Return just the name for the dog id provided."""
    return Dog.objects.get(id=dog_id).name


def pull_dog_day_id(date_instance):
    """Return the ID associated with DogDay that matches requested date."""
    dog_day = grab_correct_dog_day(date_instance)
    return dog_day.id


def format_list_of_dogs(dogs):
    """
    Return correct string of dogs for view.

    Take in query set of dogs for specific day, if empty set, return
    appropriate sentence, otherwise, return a comma separated list of dogs
    """
    if dogs.count() == 0:
        dog_list = 'Sorry, there are no dogs here today'
        # amuse self later with global list and randomized result pull
    else:
        dog_list = ', '.join(d.name for d in dogs)
    return dog_list
