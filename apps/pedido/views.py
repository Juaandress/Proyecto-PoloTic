from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
from .forms import pedidoForm,finPedidoForm

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
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instancia=form.save()
            instancia.vendedor=request.user.vendedor
            instancia.save()
            form.save_m2m()
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

class Modificar_pedido(generic.UpdateView):
    template_name='Pedidos/Modificar_pedido.html'
    model=models.pedido
    form_class=pedidoForm
    success_url = reverse_lazy('pedido:listar')
    def form_valid(self,form):
        form.save()
        form.save_m2m()
        return super(Modificar_pedido,self).form_valid(form)

class Finalizar_pedido(generic.UpdateView):
    template_name='Pedidos/Modificar_pedido.html'
    model=models.pedido
    form_class=finPedidoForm
    success_url = reverse_lazy('pedido:listar')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instancia=form.save()
            instancia.tecnico=request.user.tecnico
            instancia.save()
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

class Borrar_pedido(generic.DeleteView):
    model = models.pedido
    template_name = 'Pedidos/Borrar_pedido.html'
    success_url = reverse_lazy('pedido:listar')

class verPedido(generic.DetailView): #Ver un turno en especifico
    model = models.pedido
    template_name= 'Pedidos/detail.html'