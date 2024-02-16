from django.contrib import admin
from django.urls import path, include
from users.views import register_profile
from .views import pagina_estab


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_profile, name='profile'),
    path('pagina_estab/<int:info_especifica>/', pagina_estab, name='pagina_estab'),
]
