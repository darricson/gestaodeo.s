from ctypes.wintypes import PRECT
from pickle import TRUE
from re import VERBOSE
from django.db.models import Sum, F, ExpressionWrapper
from django.db import models
from dep_pessoal.models import Funcionario

# Create your models here.
class Vehicle(models.Model):
    modelo = models.CharField(verbose_name='MODELO', max_length=30, null=False)
    collor = models.CharField(verbose_name='COR', max_length=30)
    year = models.IntegerField(verbose_name='ANO')
    autonomy = models.IntegerField(verbose_name='AUTONOMIA/CONSUMO', null=False)
    
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.modelo = self.modelo.upper()
        self.collor = self.collor.upper()

        super(Vehicle,self).save(*args,**kwargs)
    
    
    class Meta:
        verbose_name = 'VEICULO'
        verbose_name_plural = 'VEICULOS'
        
    def __str__(self):
        return self.modelo


class Condutor(models.Model):
    conductor = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='MOTORISTA', related_name='CONDUTOR')
    vehicle = models.ForeignKey(Vehicle, related_name='VEICULO', verbose_name='VEICULO', on_delete=models.PROTECT)    
    
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.conductor = self.conductor.upper()
        self.vehicle = self.vehicle.upper()

        super(Condutor,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'CONDUTOR'
        verbose_name_plural = 'CONDUTORES'
        
    def __str__(self):
        return str(self.conductor)

class ControleKm(models.Model):
    condutor = models.ForeignKey(Condutor, verbose_name='MOTORISTA', on_delete=models.PROTECT)
    da_ta = models.DateField('DATA')
    km_init = models.IntegerField(verbose_name='KM INICIAL', null=False)
    km_end = models.IntegerField(verbose_name='KM FINAL', null=False)
    tot_km = models.IntegerField(verbose_name='KM RODADO', blank=TRUE, null=TRUE)
    
    '''
    def km_rodado(self):
        tot = ControleKm_set.all().aggregate(
            tot_totkm=Sum((F('km_end')- F('km_init'), output_field=IntegerField()))
            
        )
    
    '''
    class Meta:
        verbose_name = 'CONTROLE DE KM'
        verbose_name_plural = 'CONTROLE DE KMs'
        
    def __str__(self):
        return str(self.da_ta)
