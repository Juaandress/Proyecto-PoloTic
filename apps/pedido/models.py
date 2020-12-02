from django.db import models
from apps.paciente.models import paciente
from apps.user.models import tecnico,vendedor
# Create your models here.


class producto(models.Model):
    distancia_choice=[('L','Lejos'),('C','Cerca')]
    lado_choice=[('I','Izquierda'),('D','Derecha')]
    nombre=models.CharField(max_length=60)
    clasificacion=models.CharField(max_length=60)
    distancia=models.CharField(max_length=2,choices=distancia_choice,null=True,blank=True)
    lado=models.CharField(max_length=2,choices=lado_choice,null=True,blank=True)
    armazon=models.BooleanField(default=False,null=True,blank=True)
    precio = models.FloatField(default=0)

class pedido(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(vendedor,on_delete=models.SET_NULL, null=True, blank=True)
    tecnico = models.ForeignKey(tecnico,on_delete=models.SET_NULL, null=True, blank=True)
    productos = models.ManyToManyField(producto,related_name="pedidos_tiene",blank=True)
    descripcion = models.TextField()
    fecha = models.DateField(null=True, blank=True)
    subtotal = models.FloatField(default=0)
    tipo_pago = models.CharField(max_length=30)
    Finalizado = models.BooleanField(default=False)