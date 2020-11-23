from django.db import models
from apps.paciente.models import paciente

# Create your models here.

class pedido(models.Model):
    dni_paciente = models.ForeignKey(paciente, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(max_length=60)
    fecha = models.DateField(null=True, blank=True)
    precio = models.CharField(max_length=10)
    subtotal = models.CharField(max_length=10)
    tipo_pago = models.CharField(max_length=30)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.dni_paciente

    