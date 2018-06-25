"""All processing functions for rendering views"""

from datetime import datetime
from AltviaDogs.models import Dog
from AltviaDogs.models import Owner
from AltviaDogs.models import DogDay


def select_and_test_date(todays_date):
    date = todays_date
    # need to find date and Days
    # then test for Sat or sun
    current_date = 'date corrected'
    return current_date


def grab_list_of_dogs(select_and_test_date()):
    date = select_and_test_date()
    # test to see if record exists for this date
    # if not - create date
    dogs = Dog.objects.filter(date)
    # probably need test for if no dogs then return 'no dogs'
    # create sort order within logic (assign dog 1, dog 2, dog 3 for layout?)
    return dogs
