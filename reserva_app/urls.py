from django.contrib import admin
from django.urls import path, include
from .views import login, init_page

app_name = 'reserva_app'

urlpatterns = [
    path('', login, name='login'),
    path('init_page', init_page, name='init_page'),
]
