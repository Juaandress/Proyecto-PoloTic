from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class tecnico(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

class secretaria(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

class medico(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

class vendedor(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)