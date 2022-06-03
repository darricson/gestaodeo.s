from django.db import models

# Create your models here.
class CronogramaOsInstalacao(models.Model):
    STATUS_CHOICES = [
        ('AGENDADO', 'AGENDADO'),
        ('NÃO INICIADO', 'NÃO INICIADO'),
        ('INICIADO', 'INICIADO'),
        ('PAUSADO', 'PAUSADO'),
        ('FINALIZADO', 'FINALIZADO'),
        ('ENTREGUE', 'ENTREGUE'),
    ]
    
    SERVICE_CHOICES = [
        ('CFTV', 'CFTV'),
        ('CFTV - ALARME', 'CFTV - ALARME'),
        ('CFTV - CERCA E.', 'CERCA E.'),
        ('CFTV - CONTROLE DE ACE.', 'CFTV - CONTROLE DE ACE.'),

        ('ALARME', 'ALARME'),
        ('ALARME - CERCA E.', 'ALARME - CERCA E.'),
        ('ALARME - CONTROLE DE ACE.', 'ALARME - CONTROLE DE ACE.'),

        ('CERCA ELÉTRICA', 'CERCA ELÉTRICA'),
        ('CERCA E. - CONTROLE DE ACE.', 'CERCA E. - CONTROLE DE ACE.'),
        
        ('CONTROLE DE ACESSO', 'CONTROLE DE ACESSO'),
        
        ('ALARME - CERCA - CONT. ACE. - CFTV', 'ALARME - CERCA - CONT. ACE. - CFTV'),
        
    ]
    
    n_os = models.IntegerField(verbose_name='Nº O.S', blank=False)
    code_client = models.CharField(verbose_name='COD - Cliente', max_length=40, blank=False)
    team = models.CharField(verbose_name='Equipe', max_length=50, blank=False)
    date_start = models.DateField(verbose_name='Data Inicio')
    date_end = models.DateField(verbose_name='Data Fim')
    date_delivery = models.DateField(verbose_name='Data Entrega')
    status = models.CharField(verbose_name='Status', max_length=15, choices=STATUS_CHOICES,                              
                              default='NÃO INICIADO')
    service = models.CharField(verbose_name='Serviço(s)', max_length=40, choices=SERVICE_CHOICES,                              
                              default='ALARME')
        
    class Meta:
        verbose_name = 'CONTROLE DE O.S'
        verbose_name_plural = 'CONTROLE DE O.S'
        
    def __str__(self):
        return str(self.n_os)
    