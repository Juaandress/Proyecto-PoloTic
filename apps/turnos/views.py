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
from .forms import turnosForm
from apps.utils.funciones import PermisosMixin





# Create your views here.


def Render_html(request):
    return render(request,'Turnos/turnos.html')
    
    
class turnoList(LoginRequiredMixin, ListView):  #Ver todos los turnos
    model = turnos
    template_name = 'Turnos/listar.html'

class verTurnoEsp(LoginRequiredMixin, DetailView): #Ver un turno en especifico
    model = turnos
    template_name= 'Turnos/detail.html'

class turnoCreation(LoginRequiredMixin, PermisosMixin,CreateView):
    rol='secretaria'
    model = turnos
    success_url = reverse_lazy('turnos:listar')
    template_name= 'Turnos/cargar.html'
    form_class=turnosForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            instancia=form.save(commit=False)
            instancia.secretaria=request.user.secretaria
            instancia.save()
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

class turnoUpdate(LoginRequiredMixin,PermisosMixin, UpdateView):
    rol='secretaria'
    model = turnos
    template_name= 'Turnos/modificar.html'
    success_url = reverse_lazy('turnos:listar')
    form_class=turnosForm
    
class turnoDelete(LoginRequiredMixin,PermisosMixin, DeleteView):
    rol='secretaria'
    model = turnos
    template_name= 'Turnos/borrar.html'
    success_url = reverse_lazy('turnos:listar')



