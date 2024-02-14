from django.contrib import admin
from django.urls import path, include
from users.views import register_profile


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_profile, name='profile')
]
