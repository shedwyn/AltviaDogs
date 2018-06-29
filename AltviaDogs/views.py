"""Page rendering functions for AltviaDogs

Includes use of User to authenticate and authorize.
"""

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import JsonResponse
from django.shortcuts import render
from . import logic
# from . import settings
from .models import Dog
from datetime import date


def render_index_page(request):
    """
    render home/menu page with today's list of dogs and an input field
    allowing User to select and view a different date
    """
    curr_date = logic.determine_correct_date(date.today())
    # stub - can I dip into a variable from another module?
    # weekday = logic.list_of_weekday_values[weekday(year, month, newday)]
    dogs = logic.grab_list_of_dogs(curr_date)
    page_fill = {'date': curr_date, 'dogs': dogs}
    # page_fill = {'date': curr_date, 'dogs': dogs, 'weekday':weekday}
    return render(request, 'AltviaDogs/index.html', page_fill)

def render_view_days_dogs_page(request):
    """
    render the view_days_dogs page by taking in in date and returns list of
    that day's dogs
    """
    # how will date be received from User - in what format?
    selected_date=date(request.selected_date)
    corrected_date=logic.determine_correct_date(selected_date)
    dogs = logic.grab_list_of_dogs(corrected_date)
    # dog_day_id = logic.grab_dog_day_id_for_selected_date(corrected_date)
    page_fill = {'date':corrected_date, 'dogs':dogs}
    # page_fill = {'date':corrected_date, 'dogs':dogs, 'dog_day_id':dog_day_id}
    return render(request, 'AltviaDogs/view_days_dogs', page_fill)
