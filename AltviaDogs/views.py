"""
Designed and built by Erin 'Ernie' L. Fough.

June 2018 (start)
contact: shedwyn@gmail.com
want to know when this was last updated?  See README.md.

Page rendering functions for AltviaDogs.

Includes use of User to authenticate and authorize.

"""

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import JsonResponse
from django.shortcuts import render
from . import logic
# from . import settings
from datetime import date


def render_index_page(request):
    """
    Render home/menu page with today's list of dogs.

    Include an input field allowing User to select and view a different date.
    """
    curr_date = logic.determine_correct_date(date.today())
    dogs = logic.grab_scheduled_dogs(curr_date)
    dog_list = logic.format_list_of_dogs(dogs)
    page_fill = {'date': curr_date, 'dog_list': dog_list}
    # page_fill = {'date': curr_date, 'dogs': dogs, 'weekday':weekday}
    return render(request, 'AltviaDogs/index.html', page_fill)


def render_view_days_dogs_page(request):
    """
    Render the view_days_dogs page.

    Take in in date checks to ensure it is not a weekend date then returns
    formatted list of that day's dogs along with lists of dogs scheduled
    and not-scheduled for editing purposes
    """
    if request.POST['date_choice']:
        raw_date = tuple(
            int(item) for item in request.POST['date_choice'].split('-')
        )
        formatted_date = date(raw_date[0], raw_date[1], raw_date[2])
        corrected_date = logic.determine_correct_date(formatted_date)
        dog_day_id = logic.pull_dog_day_id(corrected_date)
    else:
        dog_day_id = request.POST['dog-day-id']

    scheduled_dogs = logic.grab_scheduled_dogs(corrected_date)

    not_scheduled_dogs = logic.grab_not_scheduled_dogs(corrected_date)

    dog_list = logic.format_list_of_dogs(scheduled_dogs)
    page_fill = {
        'date': corrected_date,
        'dog_list': dog_list,
        'scheduled_dogs': scheduled_dogs,
        'not_scheduled_dogs': not_scheduled_dogs,
        'dog_day_id': dog_day_id
    }
    return render(request, 'AltviaDogs/view_days_dogs.html', page_fill)


def render_confirm_dog_change_page_add(request):
    """Render the confirmation page for adding dogs.

    take in request containing the dog instances selected from the View page"
    """
    dog_id = request.POST['dog_to_add']
    dog_day_id = request.POST['dog_day_id']
    logic.add_dog_to_dog_day(dog_day_id, dog_id)
    curr_date = logic.grab_date_for_dog_day(dog_day_id)
    dog_names = logic.pull_correct_dog_name(dog_id)
    type_note = 'added to'
    page_fill = {
        'dog_names': dog_names,
        'type_note': type_note,
        'date': curr_date,
        'dog_day_id': dog_day_id
    }
    return render(request, 'AltviaDogs/confirm_dog_change.html', page_fill)


def render_confirm_dog_change_page_remove(request):
    """Render the confirmation page for dog changes.

    take in request containing the dog instance selected from the View page"
    """
    dog_id = request.POST['dog_to_remove']
    dog_day_id = request.POST['dog_day_id']
    logic.remove_dog_from_dog_day(dog_day_id, dog_id)
    curr_date = logic.grab_date_for_dog_day(dog_day_id)
    dog_names = logic.pull_correct_dog_name(dog_id)
    type_note = 'removed from'
    page_fill = {
        'dog_names': dog_names,
        'type_note': type_note,
        'date': curr_date,
        'dog_day_id': dog_day_id
    }
    return render(request, 'AltviaDogs/confirm_dog_change.html', page_fill)
