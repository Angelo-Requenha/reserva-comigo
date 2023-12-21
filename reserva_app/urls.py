from django.contrib import admin
from django.urls import path, include
from .views import login

app_name = 'reserva_app'

urlpatterns = [
    path('', login, name='login'),
]