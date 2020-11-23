from django import forms
from django.db import models
from .models import turnos


class registerturno(forms.ModelForm):

    fecha = forms.DateField(widget=forms.DateInput(
        attrs={"placeholder": "dia/mes/año"}))

    secretaria = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Secretaria"}))

    asistencia = forms.CharField(max_length=60, widget=forms.Textarea(
        attrs={"placeholder": "Asistencia"}))

    class Meta():
        model = turnos
        fields = ['fecha', 'secretaria', 'asistencia']