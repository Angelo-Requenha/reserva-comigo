from django.urls import handler404
from main.views import custom_404_view

# Configuração do handler404
handler404 = custom_404_view
