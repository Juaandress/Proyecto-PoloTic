from django.contrib import admin
from .models import pedido,producto
# Register your models here.

class pedidoAdmin(admin.ModelAdmin):
    pass
admin.site.register(pedido, pedidoAdmin)
class productoAdmin(admin.ModelAdmin):
    pass
admin.site.register(producto, productoAdmin)