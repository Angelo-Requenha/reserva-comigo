from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    TIPOS_USUARIO = [
        ('cliente', 'Cliente'),
        ('estabelecimento', 'Estabelecimento'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO)

    def __str__(self):
        return self.username
