from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from .views import pagina_estab
=======
from users.views import register_address
>>>>>>> dev


app_name = 'estab_app'

urlpatterns = [
<<<<<<< HEAD
    path('pagina_estab/<str:info_especifica>/', pagina_estab, name='pagina_estab'),
=======
    path('profile', register_address, name='profile')
>>>>>>> dev
]
