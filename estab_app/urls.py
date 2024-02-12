from django.contrib import admin
from django.urls import path, include
from users.views import profile_view


app_name = 'estab_app'

urlpatterns = [
    path('profile', profile_view, name='profile')
]
