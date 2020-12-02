from django.db import models
from datetime import date
from apps.user.models import medico
# from apps.user.models import medico

# Create your models here.

class paciente(models.Model):
    dni_paciente = models.IntegerField()
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    fecha = models.DateField(null=True, blank=True)

class historial_medico(models.Model):
    paciente = models.OneToOneField(paciente,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField(default=date.today,blank=True)
    medico = models.ManyToManyField(medico,related_name="modifica",blank=True)
