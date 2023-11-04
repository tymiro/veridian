from django.shortcuts import render
from fight.views import countdown

def home(request):
    """ Main page for app Home """
    return render (request, 'home/home.html')

def countdown(request):
    return render (request, 'home/base.html')