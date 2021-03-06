# chat/routing.py
from django.conf.urls import url
from django.urls import path,include
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<id1>[^/]+)/(?P<id2>[^/]+)/$', consumers.ChatConsumer),

]