from django.forms import ModelForm
from .models import historial_medico
from django.db import transaction

class ModHistorialForm(ModelForm):
    class Meta:
        model=historial_medico
        fields=['descripcion']

    def __init__(self, *args, **kwargs):
        super(ModHistorialForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
