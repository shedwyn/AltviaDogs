"""Administrator Registration Document"""


from django.contrib import admin
from . import models


admin.site.register(models.Dog)
admin.site.register(models.Owner)
# admin.site.register(models.DogDay)
