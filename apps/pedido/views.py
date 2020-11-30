from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
from .forms import pedidoForm

def Render_html(request):
    return render(request,'Pedidos/pedidos.html')


class Listar(generic.ListView):
    model = models.pedido
    template_name = "Pedidos/listar.html"
    
class ListarProducto(generic.ListView):
    model = models.producto
    template_name = "Pedidos/productos.html"
    
class Cargar_pedido(generic.CreateView):
    template_name='Pedidos/Cargar_pedido.html'
    model=models.pedido
    form_class=pedidoForm
    success_url = reverse_lazy('pedido:listar')