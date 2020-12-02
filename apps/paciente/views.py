from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.funciones import PermisosMixin
from django.urls import reverse_lazy
from .forms import ModHistorialForm

# Create your views here.

class Listar(LoginRequiredMixin, generic.ListView):
    model = models.paciente
    template_name = "Pacientes/listar.html"
    
class Ver(LoginRequiredMixin,generic.DetailView):
    model= models.paciente
    template_name = "Pacientes/detail.html"

class VerHistorial(LoginRequiredMixin,generic.DetailView):
    model= models.historial_medico
    template_name = "Pacientes/detail_historial.html"

class ModHistorial(LoginRequiredMixin,PermisosMixin,generic.UpdateView):
    model=models.historial_medico
    form_class=ModHistorialForm
    success_url=reverse_lazy('paciente:listar')
    template_name="Pacientes/modhistorial.html"
    rol='medico'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.medico.add(request.user.medico)
        return super().get(request, *args, **kwargs)
