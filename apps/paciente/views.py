from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Listar(LoginRequiredMixin, generic.ListView):
    model = models.paciente
    template_name = "Pacientes/listar.html"
    


