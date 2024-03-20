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
from django.http import HttpResponse
import matplotlib.pyplot as plt
from record.models import Position
from matplotlib.dates import YearLocator
import numpy as np
def graph_day(request, position_id):
    # Obtén las evaluaciones para el puesto de trabajo
    evaluations = Position.objects.get(id=position_id).lightingevaluation_set.filter(period="Dia").order_by('date')

    # Crea una figura y un eje con fondo transparente
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.set_facecolor('darkblue')

    # Extrae los años y los promedios de las evaluaciones
    years = [evaluation.date.year for evaluation in evaluations]
    averages = [evaluation.average for evaluation in evaluations]
    parameters = [evaluation.parameter for evaluation in evaluations]

    # Crea el gráfico de barras
    bars = ax.bar(years, averages, color='orange', edgecolor='white', label='Promedio')

    # Añade la línea del parámetro al final
    parameter = parameters[0] if len(parameters) == 1 else parameters[-1]
    ax.hlines(y=parameter, xmin=min(years)-1, xmax=max(years)+1, colors='white', linestyles='--', linewidth=2.0, label='Parámetro')

    ax.legend()

    # Añade títulos y etiquetas
    ax.set_title('Fluctuación del promedio de las evaluaciones de día', color='white')
    ax.set_xlabel('Año', color='white')
    ax.set_ylabel('Valor', color='white')

    # Configura el eje x para mostrar solo los años
    ax.set_xticks(years)
    ax.set_xticklabels(years, color='white')

    # Cambia el color de los ejes a blanco
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.xaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')

    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='y', colors='white')

    # Añade el año debajo de cada barra
    for year, bar in zip(years, bars):
        ax.text(bar.get_x() + bar.get_width()/2, -0.05, year, ha='center', va='bottom', color='white')

    # Crea un objeto HttpResponse con el tipo de contenido correcto
    response = HttpResponse(content_type='image/png')

    # Guarda la figura en el objeto HttpResponse
    fig.savefig(response, format='png', transparent=True)

    return response

def graph_night(request, position_id):
    # Obtén las evaluaciones para el puesto de trabajo
    evaluations = Position.objects.get(id=position_id).lightingevaluation_set.filter(period="Noche").order_by('date')

    # Crea una figura y un eje con fondo transparente
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.set_facecolor('darkblue')

    # Extrae los años y los promedios de las evaluaciones
    years = [evaluation.date.year for evaluation in evaluations]
    averages = [evaluation.average for evaluation in evaluations]
    parameters = [evaluation.parameter for evaluation in evaluations]

    # Crea el gráfico de barras
    bars = ax.bar(years, averages, color='orange', edgecolor='white', label='Promedio')

    # Añade la línea del parámetro al final
    parameter = parameters[0] if len(parameters) == 1 else parameters[-1]
    ax.hlines(y=parameter, xmin=min(years)-1, xmax=max(years)+1, colors='white', linestyles='--', linewidth=2.0, label='Parámetro')

    ax.legend()

    # Añade títulos y etiquetas
    ax.set_title('Fluctuación del promedio de las evaluaciones de noche', color='white')
    ax.set_xlabel('Año', color='white')
    ax.set_ylabel('Valor', color='white')

    # Configura el eje x para mostrar solo los años
    ax.set_xticks(years)
    ax.set_xticklabels(years, color='white')

    # Cambia el color de los ejes a blanco
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.xaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')

    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='y', colors='white')

    # Añade el año debajo de cada barra
    for year, bar in zip(years, bars):
        ax.text(bar.get_x() + bar.get_width()/2, -0.05, year, ha='center', va='bottom', color='white')

    # Crea un objeto HttpResponse con el tipo de contenido correcto
    response = HttpResponse(content_type='image/png')

    # Guarda la figura en el objeto HttpResponse
    fig.savefig(response, format='png', transparent=True)

    return response
