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
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    def __str__(self):
        return self.email

class UserProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    endereco = models.CharField(verbose_name="Endereço", max_length=255, blank=True, null=True)
    pais = models.CharField(verbose_name="País", max_length=255, blank=True, null=True)
    cep = models.CharField(verbose_name="CEP", max_length=9, blank=True, null=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)

    has_profile = models.BooleanField(default = False)
	
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.email}'
