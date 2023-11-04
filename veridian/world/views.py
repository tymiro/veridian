from django.shortcuts import render
from team.models import Character

def main(request):
    user_character = Character.objects.filter(user=request.user).first()
    user_character_exists = user_character is not None
    return render(request, 'world/main.html', {'user_character_exists': user_character_exists})
