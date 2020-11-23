from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import registerpedido
from .models import pedido

# Create your views here.


@login_required
def mostrar_pedidos(request):
    busqueale = request.GET.get("buscar")
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    todos = pedido.objects.filter(id_usuario=user.id).order_by("fecha")
    if busqueale:
        todos = pedido.objects.filter(
            Q(fecha__icontains=busqueale) | Q(fecha=busqueale) | Q(descripcion=busqueale) | Q(descripcion__icontains=busqueale) | Q(estado=busqueale) | Q(estado__icontains=busqueale)).distinct()
        ctx = {"user": user, "pedidos": todos}
        return render(request, "", ctx) #Aca debemos poner el URL al template de busqueda de pedidos
    ctx = {"user": user, "pedidos": todos}
    return render(request, "", ctx) #Aca debemos poner el URL al template de busqueda de pedidos


@ login_required
def edit(request, pk):
    buscar = pedido.objects.get(id=pk)
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id) #Esto tengo que verlo mas adelante, en plan de borrarlo.
        nuevopedido = registerpedido(request.POST)
        model = pedido
        # print(nuevopedido.color)
        if nuevopedido.is_valid():
            model.descripcion = nuevopedido.cleaned_data["descripcion"]
            model.fecha = nuevopedido.cleaned_data["fecha"]
            model.precio = nuevopedido.cleaned_data["precio"]
            model.subtotal = nuevopedido.cleaned_data["subtotal"]
            model.tipo_pago = nuevopedido.cleaned_data["tipo_pago"]
            model.estado = nuevopedido.cleaned_data["estado"]

            grabar = pedido(id_usuario=user, titulo=model.titulo, fecha=model.fecha, color=model.color,
                          descripcion=model.descripcion)
            grabar.save()
            return redirect('home')
        else:
            return render(request, "", {"pedido": nuevopedido}) #Aca debemos poner el URL al template de edit de pedidos
    else:
        print("enviar formulario")
        nuevopedido = registerpedido(instance=buscar)
        return render(request, "", {"pedido": nuevopedido}) #Aca debemos poner el URL al template de edit de pedidos


@ login_required
def deletepedido(request, pk):
    buscar = pedido.objects.get(id=pk)
    if request.method == "POST":
        grabar = pedido(id=buscar.id, id_usuario=buscar.id_usuario, titulo=buscar.titulo, fecha=buscar.fecha,
                      descripcion=buscar.descripcion, color=buscar.color)
        grabar.delete()
        return redirect('home')
    else:
        print("enviar formulario")
        nuevopedido = registerpedido(instance=buscar)
    return render(request, "", {"pedido": nuevopedido}) #Aca debemos poner el URL al template de borrar de pedidos


@login_required
def nuevopedido(request):
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        model = pedido
        nuevopedido = registerpedido(request.POST)
        if nuevopedido.is_valid():
            print("entro")
            model.descripcion = nuevopedido.cleaned_data["descripcion"]
            model.fecha = nuevopedido.cleaned_data["fecha"]
            model.precio = nuevopedido.cleaned_data["precio"]
            model.subtotal = nuevopedido.cleaned_data["subtotal"]
            model.tipo_pago = nuevopedido.cleaned_data["tipo_pago"]
            model.estado = nuevopedido.cleaned_data["estado"]

            grabar = pedido(id_usuario=user, titulo=model.titulo, fecha=model.fecha, color=model.color,
                          descripcion=model.descripcion)
            grabar.save()
            return redirect('home')
        else:
            return redirect('create', {"registerpedido": registerpedido})
    else:
        nuevopedido = registerpedido()
    return render(request, '', {"registerpedido": registerpedido}) #Aca debemos poner el URL al template de crear de pedidos

@login_required
def PoloTIC(request):
    return render(request, "", {}) #Aca debemos poner el URL al template de nuestro grupo.

