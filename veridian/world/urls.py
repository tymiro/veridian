""" Defines URL patterns for World. """

from django.urls import path

from . import views

app_name = "world"
urlpatterns = [
    path('main/', views.main , name='main')
]
