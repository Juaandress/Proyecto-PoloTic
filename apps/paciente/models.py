from django.db import models
# from apps.user.models import medico

# Create your models here.

class paciente(models.Model):
    dni_paciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

# class historial_medico(models.Model):
#     medico = models.ForeignKey(medico, on_delete=models.SET_NULL, null=True, blank=True)
#     descripcion = models.CharField(max_length=300)