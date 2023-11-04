from django.urls import path
from . import views

app_name = 'blacksmith'

urlpatterns = [
    path('blacksmith/', views.blacksmith, name='blacksmith'),
]
