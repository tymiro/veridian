from django.shortcuts import render

def cities(request):
    return render(request, 'cities/cities.html')
