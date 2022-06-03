from django.contrib import admin
from .models import Departamento, Funcao

# Register your models here.
admin.site.site_header = 'SICI - ÁLAMO'


class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('name_function',)
    search_fields = ('name_function',)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('name_dep',)
    search_fields = ('name_dep',)


admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)


