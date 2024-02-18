# models.py
from django.db import models


class DataDisponibilidade(models.Model):
    data = models.DateField()
    disponivel = models.BooleanField(default=True)