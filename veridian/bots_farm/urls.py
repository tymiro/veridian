from django.urls import path
from . import views

app_name = 'bots_farm'
urlpatterns = [
    path('bots_farm/', views.enemies_list, name='bots_farm'),
    path('region_selection/', views.region_selection, name='region_selection'),
]