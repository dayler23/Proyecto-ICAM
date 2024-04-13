from django.shortcuts import render, redirect
from record.models import Position
from .forms import RuidoEvaluationForm

def evaluacion_ruido(request, position_id):
    position = Position.objects.get(id=position_id)
    if request.method == 'POST':
        form = RuidoEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.position = position
            evaluation.save()
            # Redirige directamente a la página de la posición
            return redirect('position', position_id=position.id)
    else:
        form = RuidoEvaluationForm()
    context = {'position': position, 'form': form}
    return render(request, 'evaluacion_ruido.html', context)
