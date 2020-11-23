from django.contrib import admin
from .models import paciente
# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(paciente, pacienteAdmin)
