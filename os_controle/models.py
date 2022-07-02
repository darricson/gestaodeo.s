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
    central = models.IntegerField(verbose_name='CENTRAL DE ALARME', default=0)
    fonte = models.IntegerField(verbose_name='FONTE DE ALIMENTAÇÃO', default=0)
    ivp = models.IntegerField(verbose_name='SENSOR DE PRESENÇA', default=0)
    mag = models.IntegerField(verbose_name='SENSOR DE MAGNETICO', default=0)
    iva = models.IntegerField(verbose_name='SENSOR DE BARREIRA', default=0)
    dvr = models.IntegerField(verbose_name='DVR/NVR', default=0)
    cam = models.IntegerField(verbose_name='CÂMERA', default=0)
    eletrific = models.IntegerField(verbose_name='CENTRAL DE CHOQUE', default=0)
    haste_cerca = models.IntegerField(verbose_name='HASTE DE CERCA', default=0)
    leit_digita = models.IntegerField(verbose_name='LEITOR DIGITAL/FACIAL', default=0)
    eletroi = models.IntegerField(verbose_name='ELETROIMÃ', default=0)
    boto = models.IntegerField(verbose_name='BOTOEIRA', default=0)
    radio = models.IntegerField(verbose_name='RADIO OUTDOOR', default=0)
    interphon = models.IntegerField(verbose_name='INTERFONE', default=0)
    mola_air = models.IntegerField(verbose_name='MOLA AÉREA', default=0)
    raque = models.IntegerField(verbose_name='RAQUE', default=0)
    motor_gate = models.IntegerField(verbose_name='MOTOR DE PORTÃO', default=0)


    class Meta:
        verbose_name = 'CONTROLE DE O.S'
        verbose_name_plural = 'CONTROLE DE O.S'
        
    def __str__(self):
        return str(self.n_os)
    