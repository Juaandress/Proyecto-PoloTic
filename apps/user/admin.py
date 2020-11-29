from django.contrib import admin
from .models import *

# Register your models here.
class secretariaAdmin(admin.ModelAdmin):
    pass
admin.site.register(secretaria, secretariaAdmin)
class tecnicoAdmin(admin.ModelAdmin):
    pass
admin.site.register(tecnico, tecnicoAdmin)
class medicoAdmin(admin.ModelAdmin):
    pass
admin.site.register(medico, medicoAdmin)
class vendedorAdmin(admin.ModelAdmin):
    pass
admin.site.register(vendedor, vendedorAdmin)