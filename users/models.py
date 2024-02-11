from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    TIPOS = (
        ('C', 'Cliente'),
        ('E', 'Estabelecimento'),
    )
    tipo = models.CharField(max_length=1, choices=TIPOS, default='C')
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
