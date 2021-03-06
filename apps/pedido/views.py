from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
from .forms import pedidoForm,finPedidoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.funciones import PermisosMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect


def Render_html(request):
    return render(request,'Pedidos/pedidos.html')


class Listar(LoginRequiredMixin, generic.ListView):
    model = models.pedido
    template_name = "Pedidos/listar.html"
    
class ListarProducto(LoginRequiredMixin, PermisosMixin, generic.ListView):
    rol='vendedor'
    model = models.producto
    template_name = "Pedidos/productos.html"
    
class Cargar_pedido(LoginRequiredMixin, PermisosMixin, generic.CreateView):
    template_name='Pedidos/Cargar_pedido.html'
    model=models.pedido
    form_class=pedidoForm
    success_url = reverse_lazy('pedido:listar')
    rol = "vendedor"
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            instancia=form.save()
            instancia.vendedor=request.user.vendedor
            instancia.save()
            form.save_m2m()
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

class Modificar_pedido(LoginRequiredMixin, PermisosMixin, generic.UpdateView):
    rol='vendedor'
    template_name='Pedidos/Modificar_pedido.html'
    model=models.pedido
    form_class=pedidoForm
    success_url = reverse_lazy('pedido:listar')
    def form_valid(self,form):
        form.save()
        form.save_m2m()
        return super(Modificar_pedido,self).form_valid(form)

class Finalizar_pedido(LoginRequiredMixin,PermisosMixin, generic.UpdateView):
    template_name='Pedidos/Modificar_pedido.html'
    model=models.pedido
    form_class=finPedidoForm
    success_url = reverse_lazy('pedido:listar')
    rol='tecnico'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instancia=form.save()
            instancia.tecnico=request.user.tecnico
            instancia.save()
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

class Borrar_pedido(LoginRequiredMixin,PermisosMixin, generic.DeleteView):
    rol='vendedor'
    model = models.pedido
    template_name = 'Pedidos/Borrar_pedido.html'
    success_url = reverse_lazy('pedido:listar')

class verPedido(LoginRequiredMixin, generic.DetailView): #Ver un turno en especifico
    model = models.pedido
    template_name= 'Pedidos/detail.html'

def finalizar(request,pk):

    if request.user.groups.all()[0].name=='tecnico':
        pedido=models.pedido.objects.get(pk=pk)
        context={'object':pedido}
        if pedido.Finalizado:
            return render(request,'Pedidos/yata.html',context)
        if request.method=='POST':
            pedido.Finalizado=True
            pedido.tecnico=request.user.tecnico
            pedido.save()
            return HttpResponseRedirect(reverse_lazy('pedido:listar'))

        return render(request,'Pedidos/finalizar.html',context)
    raise PermissionDenied