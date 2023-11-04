from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('cities/', views.cities, name='cities'),
]
