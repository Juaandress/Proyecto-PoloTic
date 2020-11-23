from django.contrib import admin
from .models import pedido
# Register your models here.

class pedidoAdmin(admin.ModelAdmin):
    pass
admin.site.register(pedido, pedidoAdmin)