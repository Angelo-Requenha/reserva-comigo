from django.contrib import admin
from django.urls import path, include
from .views import helloworld

app_name = 'reserva_app'

urlpatterns = [
    path('', helloworld, name='helloworld'),
]