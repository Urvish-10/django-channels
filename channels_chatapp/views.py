from django.shortcuts import render


# Create your views here.
# ws://127.0.0.1:8000/ws/chat/urv/

def home(request):
    return render(request, "home.html")


def room(request, room_name):
    return render(request, "chat_room.html", {"roomname": room_name})
