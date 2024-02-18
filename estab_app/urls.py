from django.contrib import admin
from django.urls import path, include
from users.views import register_profile
from .views import pagina_estab, salvar


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_profile, name='profile'),
    path('pagina_estab/<str:info_especifica>/', pagina_estab, name='pagina_estab'),
    path('salvar', salvar, name='salvar'),
]
