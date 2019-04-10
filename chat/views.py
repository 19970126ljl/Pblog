# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='pblog:login')
def index(request):
    return render(request, 'chat/index.html', {})

# @login_required(login_url='pblog:login')
# def room(request, room_name):
#     print("room_name:",room_name)
#     print("json.dumps(room_name)",json.dumps(room_name))
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })


@login_required(login_url='pblog:login')
def room(request,id1,id2):
    return render(request, 'chat/room.html', {
        'id1': mark_safe(json.dumps(id1)),
        'id2': mark_safe(json.dumps(id2))
    })