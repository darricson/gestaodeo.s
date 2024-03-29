from django.db import models
from corporativo.models import Departamento, Funcao

# Create your models here.
class Funcionario(models.Model):
     
    name = models.CharField(verbose_name='NOME', max_length=30)
    name_dep = models.ForeignKey(Departamento, verbose_name='DEPARTAMENTO', on_delete=models.PROTECT)
    name_function = models.ForeignKey(Funcao, verbose_name='FUNÇÃO', on_delete=models.PROTECT)
    dataadmissao = models.DateField(verbose_name='DATA DE ADMISSÃO')
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=500)
    
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.obs = self.obs.upper()

        super(Funcionario,self).save(*args,**kwargs)

    
    class Meta:
        verbose_name= 'COLABORADOR'
        verbose_name_plural= 'COLABORADORES'
                
    def __str__ (self):
        return self.name
    
    
class Atestado(models.Model):
    name = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='NOME')
    cid = models.CharField(verbose_name='CID', max_length=8)
    function = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name='FUNÇÃO')
    date_init = models.DateField(verbose_name='DATA INICIAL')
    date_finish = models.DateField(verbose_name='DATA FINAL')
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=400)

    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.cid = self.cid.upper()
        self.obs = self.obs.upper()

        super(Atestado,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name ='ATESTADO'
        verbose_name_plural = 'ATESTADOS'
        
    def __str__ (self):
        return self.name.name
    
    
class Falta(models.Model):
    name = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='NOME')
    function = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name='FUNÇÃO')
    date_init = models.DateField(verbose_name='DATA INICIAL')
    date_finish = models.DateField(verbose_name='DATA FINAL')
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=400)
        
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.obs = self.obs.upper()

        super(Falta,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name ='Falta'
        verbose_name_plural = 'FALTAS'
            
    def __str__ (self):
        return self.name.name
    
    
class Extra(models.Model):
        
    TYPE_ATT_CHOICES = [
        
    ('MANUTENÇÃO', 'MANUTENÇÃO'),
    ('INSTALAÇÃO', 'INSTALAÇÃO',)
    ]
    
    name = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='TÉCNICO')
    client = models.CharField(verbose_name='CLIENTE', max_length=50)
    function = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name='FUNÇÃO')
    type_att = models.CharField(verbose_name='SERVIÇO', max_length=15, choices=TYPE_ATT_CHOICES)
    date_init = models.DateField(verbose_name='DATA ATENDIMENTO')
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=500)
    
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.client = self.client.upper()
        self.obs = self.obs.upper()

        super(Extra,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name ='PLANTÃO EXTRA'
        verbose_name_plural = 'PLANTÕES EXTRAS'
            
    def __str__ (self):
        return self.name.name
    
    
class DispensaLiberado(models.Model):
    name = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='NOME')
    function = models.ForeignKey(Funcao, on_delete=models.PROTECT, verbose_name='FUNÇÃO')
    date_init = models.DateField(verbose_name='DATA INICIAL')
    date_finish = models.DateField(verbose_name='DATA FINAL')
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=400)
        
    # metodo para alterar as letras para maiusculas
    def save(self, *args, **kwargs):
        self.obs = self.obs.upper()

        super(DispensaLiberado,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name ='DISPENSA / LIBERAÇÃO'
        verbose_name_plural = 'DISPENSA / LIBERAÇÃO'
            
    def __str__ (self):
        return self.name.name