from django import forms
from django.db import models
from .models import pedido

class registerpedido(forms.ModelForm):

    dni_paciente = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"placeholder": "DNI"}))    
    
    fecha = forms.DateField(widget=forms.DateInput(
        attrs={"placeholder": "dia/mes/año"}))

    descripcion = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Descripcion"}))

    subtotal = forms.IntegerField(widget=forms.Textarea(
        attrs={"placeholder": "subtotal"}))

    precio = forms.CharField(max_length=10, widget=forms.Textarea(
        attrs={"placeholder": "precio"}))

    estado = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Estado"}))

    tipo_pago = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Tipo de pago"}))

    class Meta():
        model = pedido
        fields = ['dni_paciente', 'fecha', 'descripcion', 'subtotal', 'precio', 'estado', 'tipo_pago']

