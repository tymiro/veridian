from django.urls import path
from . import views

app_name = 'jeweler'

urlpatterns = [
    path('jeweler/', views.jeweler, name='jeweler'),
]
