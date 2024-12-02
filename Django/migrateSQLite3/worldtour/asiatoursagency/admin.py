from django.contrib import admin
# we import the moldes we want to register
from .models import Tour
# Register your models here.
admin.site.register(Tour)
