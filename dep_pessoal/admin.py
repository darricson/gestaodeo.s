from django.contrib import admin
from .models import Funcionario, Atestado, Falta, Extra
# Register your models here.



class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_dep', 'name_function', 'dataadmissao',)
    search_fields = ('name',)


admin.site.register(Funcionario, FuncionarioAdmin)
# Register your models here.


class AtestadoAdmin(admin.ModelAdmin):
    fields = (('name', 'function'), 'cid', ('date_init', 'date_finish'))
    list_display = ('name', 'function', 'cid', 'date_init', 'date_finish')


admin.site.register(Atestado, AtestadoAdmin)


class FaltaAdmin(admin.ModelAdmin):
    fields = ('name', 'function', 'date_init', 'date_finish')
    list_display = ('name', 'function', 'date_init', 'date_finish')


admin.site.register(Falta, FaltaAdmin)

class ExtraAdmin(admin.ModelAdmin):
    fields = ('name', 'function', 'client', ('type_att', 'date_init'), 'obs')
    list_display = ('name', 'function', 'type_att', 'date_init',)
    search_fields = ('name',)


admin.site.register(Extra, ExtraAdmin)

admin.site.site_header = 'SICI - ÁLAMO'
admin.site.site_title = 'SICI - ADMINISTRAÇÃO'
admin.site.site_Index = 'SEJA BEM BINDO | SICI'
