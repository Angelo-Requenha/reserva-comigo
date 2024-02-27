from django.db import models


# Create your models here.
    
class DiaMarcado(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()
    dia = models.IntegerField()
    email_usuario = models.EmailField()

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
