from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'cliente_app'

urlpatterns = [
    path('grupos/', grupos, name='grupos'),
    path('feed/', feed, name='feed'),
]
