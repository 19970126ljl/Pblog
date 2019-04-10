# chat/urls.py
from django.conf.urls import url

from . import views
app_name='chat'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<id1>[^/]+)/$', views.room, name='room'),
]