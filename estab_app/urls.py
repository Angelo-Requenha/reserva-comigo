from django.contrib import admin
from django.urls import path, include
from users.views import register_profile
from .views import pagina_estab, salvar, pedido_reserva, pagina_de_notificacoes, calendario
from cliente_app.views import criar_grupo


app_name = 'estab_app'

urlpatterns = [
    path('profile', register_profile, name='profile'),
    path('pagina_estab/<int:info_especifica>/', pagina_estab, name='pagina_estab'),
    path('salvar', salvar, name='salvar'),
    path('criar_grupo/<int:info_especifica>/', criar_grupo, name='criar_grupo'),
    path('notificacoes', pagina_de_notificacoes, name='notificacoes'),
    path('pedido_reserva/<int:notificacao_id>/<str:acao>/', pedido_reserva, name='pedido_reserva'),
    path('calendario', calendario, name='calendario'),
]
