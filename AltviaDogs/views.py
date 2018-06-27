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
    """render home/menu page with all base data"""
    curr_date = logic.determine_correct_date(date.today())
    # test index.html : curr_date = (2018, 6, 22)
    # stub - can I dip into a variable from another module?
    # weekday = logic.list_of_weekday_values[weekday(year, month, newday)]
    # dogs = logic.grab_list_of_dogs(date.today())
    dogs = 'Argo'
    page_fill = {'date': curr_date, 'dogs': dogs}
    return render(request, 'AltviaDogs/index.html', page_fill)


# def index(request):
    # list_of_dogs=Dog.objects.order_by('name')
    # statement='Altvia Dogs Temporary Index Page, here are the dogs:'
    # dog_string=', '.join([d.name for d in list_of_dogs])
    # response_output=statement + '\n\n\n\n\n\n\n' + dog_string
    # return HttpResponse(response_output)
