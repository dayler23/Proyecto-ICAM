from django.shortcuts import render, redirect, get_object_or_404
from .forms import RuidoEvaluationForm
from record.models import Position

def evaluacion_ruido(request, position_id):
    position = get_object_or_404(Position, id=position_id)
    
    if request.method == 'POST':
        form = RuidoEvaluationForm(request.POST)
        print(request.POST)  # Imprime los datos POST para depuración
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.position = position
            evaluation.save()
            print("Datos guardados correctamente.")  # Mensaje de éxito
            return redirect('position', position_id=position.id)
        else:
            print(form.errors)  # Imprime los errores del formulario para depuración
            context = {'position': position, 'form': form}
            return render(request, 'evaluacion_ruido.html', context)
    else:
        form = RuidoEvaluationForm()

    context = {'position': position, 'form': form}
    return render(request, 'evaluacion_ruido.html', context)
