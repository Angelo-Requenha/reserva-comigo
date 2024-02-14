from django.contrib import admin
from django.urls import path, include
from users.views import register_address
from estab_app.views import schedule


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_address, name='profile'),
    path('schedule', schedule, name ='schedule')
]
