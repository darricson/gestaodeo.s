from django.contrib import admin
from .models import Vehicle, ControleKm, Condutor
# Register your models here.


class ControleKmInline(admin.TabularInline):
    fieldsets = [
        ('CONTROLE KM',{
            'fields':(('da_ta', 'km_init', 'km_end'), )}),
    ]
    
    model = ControleKm
    extra = 1

class CondutorAdmin(admin.ModelAdmin):
    inlines = [
        
        ControleKmInline,
        
        ]
    list_display = ('conductor', 'vehicle',)
    fieldsets = (
        ('CONDUTOR',{
            'fields':('conductor','vehicle')
            }),
    )
    
       
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'collor', 'year', 'autonomy',)
   
   
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Condutor, CondutorAdmin) 
admin.site.register(ControleKm) 


