from django.contrib import admin
from .models import ClienteOrcamento, Vistoria, Orcamento
# Register your models here.

class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('budget', 'client_client', 'consultant')
    list_filter = ('budget',)
    fieldsets = (
        ('DADOS DO ORÇAMENTO', {'fields': ('client_client', 'budget',
                                           'consultant')}),
        ('ETAPAS', {'fields':('term_survey', 'sketch', 'survey', 'alter_budget',
                              'budget_closure', 'send_dp_accept', 'acceptance_confirmation',
                              'confirmation_payment', 'releaser_installation',
                              'request_reopening', 'obs')}),
    )   

class ClienteOrcamentoAdmin(admin.ModelAdmin):
    list_display = ('client_client', 'consultant')


class VistoriaAdmin(admin.ModelAdmin):
    #fields = ('ClienteOrcamento__client_client',)
    list_display = ('budget_client', 'client_survey', 'consultant', 'status')
    fieldsets = (
        ('DADOS DA VISTORIA', {'fields':('client_survey', 'consultant', 'budget_client')}),
        ('SITUAÇÃO DA VISTORIA', {'fields':('status','date_start', 'date_fin', 'date_delivery',('alteration',
                                            'no_alteration'),)}),
        ('ALTERAÇÃO DE EQUIPAMENTOS', {'fields':('obs_eqp_alter',)}),
        ('ALTERAÇÃO IMPLANTAÇÃO', {'fields':('obs_implant_alter',)}),
        ('ALTERAÇÃO SERVIÇO', {'fields':('obs_service_alter',)}),
        ('ALTERAÇÃO INFRAESTRUTURA', {'fields':('obs_infra_alter',)}),


    )
     

admin.site.register(Orcamento, OrcamentoAdmin)
admin.site.register(ClienteOrcamento, ClienteOrcamentoAdmin)
admin.site.register(Vistoria, VistoriaAdmin)