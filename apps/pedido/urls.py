from django.urls import path
from .views import mostrar_pedidos, edit, nuevopedido, deletepedido, PoloTIC


app_name='pedidos'
urlpatterns = [
    path("home/", mostrar_pedidos, name="home"),
    path("home/home", mostrar_pedidos, name="home2"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("create/", nuevopedido, name="create"),
    path("delete/<int:pk>/", deletepedido, name="delete"),
    path("PoloTIC/", PoloTIC, name="PoloTIC"),
]
