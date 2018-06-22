"""Page rendering functions for AltviaDogs

Includes use of User to authenticate and authorize.
"""

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.http import JsonResponse
from django.shortcuts import render
# from . import logic
# from . import settings
from .models import Dog


def render_index_page(request):
    """render home/menu page with all base data"""
    page_fill = {}
    return render(request, 'AltviaDogs/index.html', page_fill)


def index(request):
    list_of_dogs = Dog.objects.order_by('name')
    statement = 'Altvia Dogs Temporary Index Page, here are the dogs:'
    dog_string = ', '.join([d.name for d in list_of_dogs])
    response_output = statement + '\n\n\n\n\n\n\n' + dog_string
    return HttpResponse(response_output)
