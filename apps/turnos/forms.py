from django.forms import ModelForm, DateInput
from .models import turnos

class turnosForm(ModelForm):
    class Meta:
        model=turnos
        fields=['secretaria','paciente','medico','fecha','asistencia']
        widgets={
            "fecha":DateInput(
                format='%d/%m/%Y',
                attrs={
            'id':'datepicker',
            'autocomplete':"off"
        })}
    def __init__(self, *args, **kwargs):
        super(turnosForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'