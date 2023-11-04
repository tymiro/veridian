from django.urls import path
from . import views

app_name = 'arena'
urlpatterns = [
    path('arena_select/', views.enemy_select, name='arena_select'),
    path('arena_fight/', views.fight, name='arena_fight'),
]