from django.shortcuts import render
from . import models


# view name should be the same as that on url.py
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
