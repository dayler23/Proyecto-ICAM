from django.shortcuts import render, redirect
from record.models import Position
from .forms import LightingEvaluationForm  # Asegúrate de importar tu formulario

def evaluacion_iluminacion(request, position_id):
    position = Position.objects.get(id=position_id)
    if request.method == 'POST':
        form = LightingEvaluationForm(request.POST)  # Crea una nueva instancia del formulario con los datos POST
        if form.is_valid():
            evaluation = form.save(commit=False)  # Crea una nueva instancia de LightingEvaluation pero no la guarda todavía
            evaluation.position = position  # Asigna el puesto de trabajo a la evaluación
            evaluation.save()  # Guarda la evaluación en la base de datos
            
            return redirect('position', position_id=position.id)  # Redirige a la página de detalle del puesto de trabajo
        else:
            print(form.errors)
    else:
        form = LightingEvaluationForm()  # Crea una nueva instancia del formulario vacía
    context = {'position': position, 'form': form}
    return render(request, 'evaluacion_iluminacion.html', context)
