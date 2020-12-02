from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q
from .models import turnos
from django.views.generic.list import ListView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.


def Render_html(request):
    return render(request,'Turnos/turnos.html')
    
    
class turnoList(LoginRequiredMixin, ListView):  #Ver todos los turnos
    model = turnos
    template_name = 'Turnos/listar.html'

class verTurnoEsp(LoginRequiredMixin, DetailView): #Ver un turno en especifico
    model = turnos
    template_name= 'Turnos/detail.html'

class turnoCreation(LoginRequiredMixin, CreateView):
    model = turnos
    success_url = reverse_lazy('turnos:listar')
    template_name= 'Turnos/turnos.html'
    fields = ['secretaria', 'paciente', 'medico', 'fecha', 'asistencia']

class turnoUpdate(LoginRequiredMixin, UpdateView):
    model = turnos
    template_name= 'Turnos/modificar.html'
    success_url = reverse_lazy('turnos:listar')
    fields = ['secretaria', 'paciente', 'medico', 'fecha', 'asistencia']
    
class turnoDelete(LoginRequiredMixin, DeleteView):
    model = turnos
    template_name= 'Turnos/borrar.html'
    success_url = reverse_lazy('turnos:listar')



