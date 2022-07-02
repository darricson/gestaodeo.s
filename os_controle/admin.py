from django.contrib import admin
from .models import CronogramaOsInstalacao


admin.site.site_header = 'SICI - ÁLAMO'

class CronogramaOsInstalacaoAdmin(admin.ModelAdmin):
    #fields = ('status', ('n_os', 'code_client'), 'team', 'service', ('date_start', 'date_end'), 'date_delivery')
    list_display = ('n_os', 'code_client', 'team', 'status', 'date_start', 'service')
    #date_hierarchy = 'date_start'
    list_filter = ('service', 'team', 'status')
    search_fields = ('code_client',)
    fieldsets = (
        ('DADOS DO SERVIÇO', {'fields':('status', ('n_os', 'code_client'), 'team', 'service', 
                                        ('date_start', 'date_end'), 'date_delivery')}),
        ('ALARME', {'fields': ('central', 'fonte', 'ivp', 'mag', 'iva')}),
        ('CFTV', {'fields':('dvr', 'cam')}),
        ('CERCA ELÉTRICA', {'fields':('eletrific', 'haste_cerca')}),
        ('CONTROLE DE ACESSO', {'fields':('leit_digita', 'eletroi', 'boto', 'radio',
                                          'interphon', 'mola_air', 'raque', 'motor_gate')})
    )
        
    def get_date_start(self, obj):
        if obj.start_date:
            return obj.start_date.strftime('%d/%m/%y')
        get_date_start.short_description = 'Inicio'

# Register your models here.
admin.site.register(CronogramaOsInstalacao, CronogramaOsInstalacaoAdmin)
