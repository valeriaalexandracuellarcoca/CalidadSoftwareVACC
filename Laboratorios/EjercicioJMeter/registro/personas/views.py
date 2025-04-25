from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/registro.html', {'form': form})

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista.html', {'personas': personas})
