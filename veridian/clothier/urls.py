from django.urls import path
from . import views

app_name = 'clothier'

urlpatterns = [
    path('clothier/', views.clothier, name='clothier'),
]
