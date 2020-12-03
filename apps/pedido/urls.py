from django.urls import path
from .views import Render_html, Listar, Cargar_pedido,Modificar_pedido,Finalizar_pedido,Borrar_pedido,verPedido, finalizar


app_name='pedido'
urlpatterns = [
    path('RenderHTML', Render_html, name='render'),
    path('Listar', Listar.as_view(), name='listar'),
    path('Cargar',Cargar_pedido.as_view(),name='cargar'),
    path('Modificar/<pk>',Modificar_pedido.as_view(),name='modificar'),
    path('Finalizar/<pk>', finalizar,name='finalizar'),
    path('Borrar/<pk>',Borrar_pedido.as_view(),name='borrar'),
    path('ver/<pk>',verPedido.as_view(),name='ver'),
    
]