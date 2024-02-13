from django.contrib import admin
from django.urls import path, include
from users.views import register_address


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_address, name='profile')
]
