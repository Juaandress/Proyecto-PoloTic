from django.contrib import admin
from .models import paciente,historial_medico
# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(paciente, pacienteAdmin)

class historialAdmin(admin.ModelAdmin):
    pass
admin.site.register(historial_medico, historialAdmin)