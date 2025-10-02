from django import forms
from django.core.exceptions import ValidationError
import datetime

#Nombre y fecha obligatorio, ubicación opcional
class EventoForm(forms.Form):
    nombre_del_evento = forms.CharField(label="Nombre del Evento", max_length=100)
    fecha = forms.DateField(label="Fecha del Evento", widget=forms.DateInput(attrs={'type': 'date'}))
    ubicacion = forms.CharField(label="Ubicación", required=False)

#Validar la fecha para que no sea en el pasado
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < datetime.date.today():
            raise ValidationError("¡La fecha del evento no puede ser en el pasado!")
        return fecha

class ParticipanteForm(forms.Form):
    nombre_del_participante = forms.CharField(label="Nombre del Participante")
    correo_electronico = forms.EmailField(label="Correo Electrónico")