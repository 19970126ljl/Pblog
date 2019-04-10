# chat/urls.py
from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='chat'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^(?P<id1>[^/]+)/(?P<id2>[^/]+)/$', views.room, name='room'),
]