from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.

class Listar(generic.ListView):
    model = models.paciente
    template_name = "Pacientes/listar.html"
    


