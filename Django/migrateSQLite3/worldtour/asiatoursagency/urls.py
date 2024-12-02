# you made this urls.py file (:
from django.urls import path
from . import views
urlpatterns =[

    path('',views.index)
]