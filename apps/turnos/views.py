from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import registerturno
from .models import turno

# Create your views here.

@login_required
def nuevoturno(request):
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        model = turno
        nuevoturno = registerturno(request.POST)
        if nuevoturno.is_valid():
            print("entro")
            model.fecha = nuevoturno.cleaned_data["fecha"]
            model.secretaria = nuevoturno.cleaned_data["secretaria"]
            model.asistencia = nuevoturno.cleaned_data["asistencia"]

            grabar = turno(fecha=model.fecha, secretaria=model.secretaria,
                          asistencia=model.asistencia)
            grabar.save()
            return redirect('home')
        else:
            return redirect('create', {"registerturno": registerturno})
    else:
        nuevoturno = registerturno()
    return render(request, 'home/create.html', {"registerturno": registerturno})


@login_required
def mostrar_turnos(request):
    busqueale = request.GET.get("buscar")
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    todos = turno.objects.filter(id_usuario=user.id).order_by("fecha")
    if busqueale:
        todos = turno.objects.filter(
            Q(fecha__icontains=busqueale) | Q(fecha=busqueale) | Q(secretaria=busqueale) | Q(secretaria__icontains=busqueale) | Q(asistencia=busqueale) | Q(asistencia__icontains=busqueale)).distinct()
        ctx = {"user": user, "turnos": todos}
        return render(request, "", ctx) #Aca debemos poner el URL al template de busqueda de turnos
    ctx = {"user": user, "turnos": todos}
    return render(request, "", ctx) #Aca debemos poner el URL al template de busqueda de turnos


@ login_required
def edit(request, pk):
    buscar = turno.objects.get(id=pk)
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id) #Esto tengo que verlo mas adelante, en plan de borrarlo.
        nuevoturno = registerturno(request.POST)
        model = turno
        # print(nuevoturno.color)
        if nuevoturno.is_valid():
            model.descripcion = nuevoturno.cleaned_data["descripcion"]
            model.fecha = nuevoturno.cleaned_data["fecha"]
            model.precio = nuevoturno.cleaned_data["precio"]
            model.subtotal = nuevoturno.cleaned_data["subtotal"]
            model.tipo_pago = nuevoturno.cleaned_data["tipo_pago"]
            model.estado = nuevoturno.cleaned_data["estado"]

            grabar = turno(id_usuario=user, titulo=model.titulo, fecha=model.fecha, color=model.color,
                          descripcion=model.descripcion)
            grabar.save()
            return redirect('home')
        else:
            return render(request, "home/edit.html", {"turno": nuevoturno})
    else:
        print("enviar formulario")
        nuevoturno = registerturno(instance=buscar)
        return render(request, "home/edit.html", {"turno": nuevoturno})


@ login_required
def deleteturno(request, pk):
    buscar = turno.objects.get(id=pk)
    if request.method == "POST":
        grabar = turno(id=buscar.id, id_usuario=buscar.id_usuario, titulo=buscar.titulo, fecha=buscar.fecha,
                      descripcion=buscar.descripcion, color=buscar.color)
        grabar.delete()
        return redirect('home')
    else:
        print("enviar formulario")
        nuevoturno = registerturno(instance=buscar)
    return render(request, "home/delete.html", {"turno": nuevoturno})

