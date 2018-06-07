"""AltviaDogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index')
    # url(r'^index_page$', views.render_index_page, name='index_page'),
    # will initially only have welcome and select datetime
    # pop up "create Tuesday, May 24, 2018"? yes/no, then create new dog_day
    # url(r'^dog_day$',views.render_dog_day,name='dog_day'),
    # view the 7 slots and any names associated with that day
    # url(r'^new_dog$,views.render_new_dog, name='new_dog'),
    # add new dog screen, needs selection list for Owners (added by Admin)
    # eventually will have ability to add a record to an individual dog
]
