from django.contrib import admin
from .models import turnos

# Register your models here.

class turnoAdmin(admin.ModelAdmin):
    pass
admin.site.register(turnos, turnoAdmin)