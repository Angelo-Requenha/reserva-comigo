from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # Login e Logout do usuário
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # Alteração de senha do usuário
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(template_name='registration/alterar_senha.html'), name='alterar_senha'),
    path('alterar_senha/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/senha_alterada.html'), name='password_change_done'),
 
    # Resetar a senha do usuário
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  

    # Cadastro de usuário
    path('register_cliente/', views.register_cliente.as_view(), name='register_cliente'),
    path('register_estab/', views.register_estab.as_view(), name='register_estab'),
]