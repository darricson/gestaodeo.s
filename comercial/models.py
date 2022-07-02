from http import client
from pickle import TRUE
from tabnanny import verbose
from django.db import models
from dep_pessoal.models import Funcionario

# Create your models here.


class ClienteOrcamento(models.Model):
    client_client = models.CharField(verbose_name='CLIENTE', max_length=80)
    budget = models.IntegerField(verbose_name='ORÇAMENTO Nº')
    consultant = models.ForeignKey(Funcionario, verbose_name='CONSULTOR', on_delete=models.PROTECT)
    term_survey = models.BooleanField(verbose_name='TERMO DE VISTORIA', default=False)
    sketch = models.BooleanField(verbose_name='CROQUI', default=False)
    survey = models.BooleanField(verbose_name='VISTORIA', default=False)
    alter_budget = models.BooleanField(verbose_name='ALTERAÇÃO ORÇAMENTO', default=False)
    budget_closure = models.BooleanField(verbose_name='FECHAMENTO DO ORÇAMENTO', default=False)
    send_dp_accept = models.BooleanField(verbose_name='ENVIO DP ACEITE', default=False)
    acceptance_confirmation = models.BooleanField(verbose_name='CONFIRMAÇÃO DE ACEITE', default=False)
    antecipation = models.BooleanField(verbose_name='ANTECIPAÇÃO', default=False)
    confirmation_payment = models.BooleanField(verbose_name='CONFIRMAÇÃO DE PAGAMENTO', default=False)
    releaser_installation = models.BooleanField(verbose_name='LIBERADO PARA INSTALAÇÃO', default=False)
    request_reopening = models.BooleanField(verbose_name='SOLICITAÇÃO PARA REABERTURA DE O.S', default=False)
    obs = models.TextField(verbose_name='OBSERVAÇÃO', max_length=1000)
    
    
    class Meta:
        verbose_name = 'CLIENTE / ORÇAMENTO'
        verbose_name_plural = 'CLIENTE / ORÇAMENTOS'
        
    
    def __str__ (self):
        return self.client_client
    
    
class Vistoria(models.Model):
    
    STATUS_CHOICES = [
        ('AGENDADO', 'AGENDADO'),
        ('NÃO INICIADO', 'NÃO INICIADO'),
        ('INICIADO', 'INICIADO'),
        ('PAUSADO', 'PAUSADO'),
        ('FINALIZADO', 'FINALIZADO'),
        ('ENTREGUE', 'ENTREGUE'),
    ]
    
    client_survey = models.ForeignKey(ClienteOrcamento,verbose_name='CLIENTE', 
                                      related_name='CLIENTE / ORÇAMENTO+', on_delete=models.PROTECT)
    consultant = models.ForeignKey(Funcionario, verbose_name='CONSULTOR', related_name='CONSULTOR', on_delete=models.PROTECT)
    budget_client = models.ForeignKey(ClienteOrcamento ,verbose_name='ORÇAMENTO Nº', related_name='ORÇAMENTO',
                                      on_delete=models.PROTECT)
    status = models.CharField(verbose_name='STATUS', max_length=15, choices=STATUS_CHOICES,                              
                              default='NÃO INICIADO')
    date_start = models.DateField(verbose_name='Data Inicio')
    date_end = models.DateField(verbose_name='Data Fim')
    date_delivery = models.DateField(verbose_name='Data Entrega')
    alteration = models.BooleanField(verbose_name='COM ALTERAÇÃO')
    no_alteration = models.BooleanField(verbose_name='SEM ALTERAÇÃO', default=True)
    # campos para registro na alterção da vistoria
    obs_eqp_alter = models.TextField(verbose_name='OBSERVAÇÃO DE EQUIPAMENTOS', max_length=1000)
    obs_implant_alter = models.TextField(verbose_name='OBSERVAÇÃO DE IMPLANTAÇÃO', max_length=1000)
    obs_service_alter = models.TextField(verbose_name='OBSERVAÇÃO DE SERVIÇO', max_length=1000)
    obs_infra_alter = models.TextField(verbose_name='OBSERVAÇÃO DE INFRAESTRUTURA', max_length=1000)

    
    def alteration_yes(self):
        if self.alteration is True:
            self.no_alteration is False
        else:
            self.no_alteration is True
        return self.alteration_yes()
    
    
    class Meta:
        verbose_name = 'VISTORIA'
        verbose_name_plural = 'VISTORIAS'
        
        
    def __str__ (self):
        return str(self.budget_client)