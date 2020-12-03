from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.funciones import PermisosMixin
from apps.turnos.models import turnos
from apps.pedido.models import pedido
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max,Count
# Create your views here.
lastmonth=timezone.now().date() - timedelta(days=30)
def Render_html(request):
    return render(request,'Reportes/reportes.html')

def asistencia_turnos(request):
    turno=turnos.objects.filter(asistencia=True, fecha__gte=lastmonth,fecha__lte=timezone.now().date())
    context={'object_list':turno}
    return render(request, 'Reportes/listar.html', context)

def no_asistencia_turnos(request):
    turno=turnos.objects.filter(asistencia=False, fecha__gte=lastmonth,fecha__lte=timezone.now().date())
    context={'object_list':turno}
    return render(request, 'Reportes/listar.html', context)

def paciente_pedido(request):
    p=pedido.objects.filter(fecha__gte=lastmonth,fecha__lte=timezone.now().date())
    context={'object_list':p}
    return render(request, 'Reportes/paciente_pedido.html', context)

def productos_mas_vendidos(request):
    p=pedido.objects.filter(fecha__gte=lastmonth,fecha__lte=timezone.now().date()).values('productos','fecha').annotate(cant_p=Count('productos')).order_by('-cant_p')
    context={'object_list':p}
    return render(request, 'Reportes/prod_vendidos.html', context)

def ventas_totales_por_mes(request):
    p=pedido.objects.values('vendedor','fecha').annotate(venta=Count('fecha'))
    context={'object_list':p}
    return render(request, 'Reportes/ventas.html', context)