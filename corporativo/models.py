from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name_dep = models.CharField(verbose_name='DEPARTAMENTO', max_length=40)
    
    class Meta:
        verbose_name = 'DEPARTAMENTO'
        verbose_name_plural = 'DEPARTAMENTOS'
    
    def __str__(self):
        return self.name_dep
    

class Funcao(models.Model):
    name_function = models.CharField(verbose_name='FUNÇÃO', max_length=40)
    
    class Meta:
        verbose_name = 'FUNÇÃO'
        verbose_name_plural = 'FUNÇÕES'
    
    def __str__(self):
        return self.name_function
