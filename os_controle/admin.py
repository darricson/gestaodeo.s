from django.contrib import admin
from .models import CronogramaOsInstalacao


admin.site.site_header = 'Álamo - Instalação'

class CronogramaOsInstalacaoAdmin(admin.ModelAdmin):
    list_display = ('n_os', 'code_client', 'team', 'status', 'date_start', 'service')
    #date_hierarchy = 'date_start'
   # list_filter = ('code_client',)
    search_fields = ('code_client',)
        
    def get_date_start(self, obj):
        if obj.start_date:
            return obj.start_date.strftime('%d/%m/%y')
        get_date_start.short_description = 'Inicio'

# Register your models here.
admin.site.register(CronogramaOsInstalacao, CronogramaOsInstalacaoAdmin)
