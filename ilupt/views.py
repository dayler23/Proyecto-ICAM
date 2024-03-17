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

#grafico
# En views.py de la aplicación iluPT
from django.http import HttpResponse
import matplotlib.pyplot as plt
from record.models import Position  # Importa el modelo Position desde la otra aplicación

def graph(request, position_id):
    # Crea una figura y un eje
    fig, ax = plt.subplots()

    # Obtén las evaluaciones para el puesto de trabajo
    evaluations = Position.objects.get(id=position_id).lightingevaluation_set.all()

    # Extrae las fechas y los promedios de las evaluaciones
    dates = [evaluation.date for evaluation in evaluations]
    averages = [evaluation.average for evaluation in evaluations]
    parameters = [evaluation.parameter for evaluation in evaluations]

    # Crea el gráfico
    ax.plot(dates, averages, label='Promedio')
    ax.plot(dates, parameters, label='Parámetro', linestyle='--*')
    ax.legend()

    # Añade títulos y etiquetas
    ax.set_title('Fluctuación del promedio de las evaluaciones')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Valor')

    # Crea un objeto HttpResponse con el tipo de contenido correcto
    response = HttpResponse(content_type='image/png')

    # Guarda la figura en el objeto HttpResponse
    fig.savefig(response, format='png')

    return response
