from django.urls import path
from .views import mostrar_pedidos, edit, nuevopedido, deletepedido, PoloTIC


app_name='pedido'
urlpatterns = [
    path("Listar", mostrar_pedidos, name="listar"),
]
