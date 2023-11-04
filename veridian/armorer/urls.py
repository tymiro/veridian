from django.urls import path
from . import views

app_name = 'armorer'

urlpatterns = [
    path('armorer/', views.armorer, name='armorer'),
]
