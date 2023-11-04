""" Defines URL patterns for Home. """

from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home')
]
