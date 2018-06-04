"""Page rendering functions for AltviaDogs

Includes use of User to authenticate and authorize.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.http import JsonResponse
from django.shortcuts import render

from . import logic
from . import settings
