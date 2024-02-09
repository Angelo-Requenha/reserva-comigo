from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'cliente_app'

urlpatterns = [
    path('grupos/', grupos, name='grupos'),
    path('feed/', feed, name='feed'),
    path('adicionar-membro/<int:grupo_id>/', adicionar_membro, name='adicionar_membro'),
    path('respond_to_friend_request/', respond_to_friend_request, name='respond_to_friend_request'),
    path('send_friend_request/', send_friend_request, name='send_friend_request'),
]
