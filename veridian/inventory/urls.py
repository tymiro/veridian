from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('equipment/', views.inventory, name='equipment'),
]
