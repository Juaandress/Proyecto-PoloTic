from django.db import models
# from apps.user.models import secretaria


# Create your models here.

class turnos(models.Model):
    fecha = models.DateField(null=True, blank=True)
    asistencia = models.BooleanField()
   
   
    # secretaria = models.ForeignKey(secretaria, on_delete=models.SET_NULL, null=True, blank=True)


