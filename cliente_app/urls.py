from django.contrib import admin
from django.urls import path, include
from .views import grupos

app_name = 'cliente_app'

urlpatterns = [
    path('grupos/', grupos, name='grupos'),
]