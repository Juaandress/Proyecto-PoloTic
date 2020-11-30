from django.forms import ModelForm,DateInput
from .models import pedido
from django.db import transaction

class pedidoForm(ModelForm):
    class Meta:
        model=pedido
        fields=['paciente','vendedor','tecnico','tipo_pago','fecha','descripcion','productos']
        widgets={
            "fecha":DateInput(
                format='%d/%m/%Y',
                attrs={
            'id':'datepicker'
        })}
    def __init__(self, *args, **kwargs):
        super(pedidoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self):
        pedido=super().save(commit=False)
        productos=self.cleaned_data['productos']
        for p in productos.all():
            pedido.subtotal+=p.precio
        pedido.save()
        return pedido
