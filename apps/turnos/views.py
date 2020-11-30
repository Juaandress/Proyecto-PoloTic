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




# Create your views here.


def Render_html(request):
    return render(request,'Turnos/turnos.html')
    
    
class turnoList(ListView):  #Ver todos los turnos
    model = turnos
    template_name = 'Turnos/listar.html'

class verTurnoEsp(DetailView): #Ver un turno en especifico
    model = turnos

class turnoCreation(CreateView):
    model = turnos
    success_url = reverse_lazy('turnos:Listar')
    fields = ['secretaria', 'paciente', 'medico', 'fecha', 'asistencia']

class turnoUpdate(UpdateView):
    model = turnos
    success_url = reverse_lazy('turnos:Listar')
    fields = ['secretaria', 'paciente', 'medico', 'fecha', 'asistencia']
    
class turnoDelete(DeleteView):
    model = turnos
    success_url = reverse_lazy('turnos:Listar')



