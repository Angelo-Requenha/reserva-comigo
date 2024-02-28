from django.contrib import admin
from django.urls import path, include
from .views import criar_grupo, grupos, feed, grupo_infos, profile_edit

app_name = 'cliente_app'

urlpatterns = [
    path('grupos/', grupos, name='grupos'),
    path('feed/', feed, name='feed'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('grupo_infos/<int:info_especifica>/<int:grupo_id>/', grupo_infos, name='grupo_infos'),
]
