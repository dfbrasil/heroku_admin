from operator import mod
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
from django.db.models import PROTECT

class Linguagem(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'linguagens'

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class Programador(models.Model):
    nome = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=8 ,decimal_places=2, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT, related_name='programadores', blank=True, null=True)
    linguagens = models.ManyToManyField(Linguagem, related_name='programadores')

    class Meta:
        verbose_name_plural = 'programadores'

    def __str__(self):
        return self.nome    
