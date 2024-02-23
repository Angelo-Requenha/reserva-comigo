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
    longitude = models.IntegerField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.IntegerField(verbose_name="Latitude",max_length=50, null=True, blank=True)

    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    capacidade_pessoas = models.PositiveIntegerField(default=0)  
    TIPOS_HORARIO = [
        ('hora', 'Por Hora'),
        ('noite', 'Por Noite'),
    ]
    tipo_horario = models.CharField(max_length=5, choices=TIPOS_HORARIO, default='hora')

    has_profile = models.BooleanField(default = False)
	
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.email}'


class FotosEstab(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    foto1 = models.ImageField(upload_to='foto_estab', blank=True, null=True)
    foto2 = models.ImageField(upload_to='foto_estab', blank=True, null=True)
    foto3 = models.ImageField(upload_to='foto_estab', blank=True, null=True)
    foto4 = models.ImageField(upload_to='foto_estab', blank=True, null=True)
    foto5 = models.ImageField(upload_to='foto_estab', blank=True, null=True)
    foto6 = models.ImageField(upload_to='foto_estab', blank=True, null=True)

    has_fotos = models.BooleanField(default = False)
	
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.email}'
    
