from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login e Logout do usuário
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # Alteração de senha do usuário
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(template_name='registration/alterar_senha.html'), name='alterar_senha'),
    path('alterar_senha/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/senha_alterada.html'), name='password_change_done'),
 
    # Resetar a senha do usuário
    path('resetar_senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('resetar_senha/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  

    # Cadastro de usuário
    path('register/', views.register, name='register'),

    path('home', views.home, name='home'),
]