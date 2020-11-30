from django.urls import path
from .views import Render_html, Listar, Cargar_pedido


app_name='pedido'
urlpatterns = [
    path('RenderHTML', Render_html, name='render'),
    path('listar', Listar.as_view(), name='listar'),
    path('Cargar',Cargar_pedido.as_view(),name='cargar'),
]