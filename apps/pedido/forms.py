from django.forms import ModelForm,DateInput
from .models import pedido


class pedidoForm(ModelForm):
    class Meta:
        model=pedido
        fields='__all__'
        
        widgets={
            "fecha":DateInput(attrs={

            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })}