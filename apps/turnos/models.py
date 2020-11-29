from django.db import models
from apps.user.models import secretaria, medico
from apps.paciente.models import paciente

# from apps.user.models import secretaria


# Create your models here.

class turnos(models.Model):
    secretaria = models.ForeignKey(secretaria, on_delete=models.CASCADE)
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)  
    medico = models.ForeignKey(medico, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    asistencia = models.BooleanField()
  
   




