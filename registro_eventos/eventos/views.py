from django.shortcuts import render
from .forms import EventoForm, ParticipanteForm

def registrar_evento(request):
    NUMERO_DE_PARTICIPANTES = 1

    if request.method == 'POST':
        
        evento_form = EventoForm(request.POST)
        participante_forms = [ParticipanteForm(request.POST, prefix=f'p{i}') for i in range(NUMERO_DE_PARTICIPANTES)]

        evento_es_valido = evento_form.is_valid()
        
        participantes_son_validos = all(p_form.is_valid() for p_form in participante_forms if p_form.has_changed())

        if evento_es_valido and participantes_son_validos:
            datos_evento = evento_form.cleaned_data
            datos_participantes = [p_form.cleaned_data for p_form in participante_forms if p_form.has_changed()]
            

            return render(request, 'registro_exitoso.html', {
                'datos_evento': datos_evento,
                'datos_participantes': datos_participantes,
            })
    
    else:
        evento_form = EventoForm()
        participante_forms = [ParticipanteForm(prefix=f'p{i}') for i in range(NUMERO_DE_PARTICIPANTES)]


    return render(request, 'registrar_evento.html', {
        'evento_form': evento_form,
        'participante_forms': participante_forms,
    })