from django.shortcuts import render,get_object_or_404,redirect

#IMPORTACION DE MODELOS PARA OBTENER DATOS
from record.models import Company,Area,Position

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from record.forms import AreaForm  # Importa el formulario de área
from mainapp.forms import CompanyForm
from django.contrib import messages
from django.urls import reverse 
from django.db.models import Q


# Create your views here.

#metodo para extraer todo el objeto de Position y mostrar en list.html
@login_required(login_url="login")
def list(request):
    # Obtén el ID de la empresa seleccionada de la sesión
    selected_company_id = request.session.get('selected_company_id')

    # Si no hay ninguna empresa seleccionada, muestra un mensaje de error
    if selected_company_id is None:
        messages.error(request, "Por favor, selecciona una empresa primero.")
        return redirect('index')

    # Obtén la empresa seleccionada
    selected_company = get_object_or_404(Company, id=selected_company_id)

    # Obtén solo las áreas de la empresa seleccionada
    areas = Area.objects.filter(company=selected_company)

    # Obtén solo los puestos de trabajo de esas áreas
    

    return render(request, 'positions/list.html', {
        'title': 'Areas',
        'areas':areas
        
    })





#metodo para extraer todo el objeto de area y mostrar los 
#positions de cada area

#muestra los puestos por area al seleccionar el area 
@login_required(login_url="login")
def area(request,area_id):
    #crea pagina de cada area
    area=get_object_or_404(Area,id=area_id)

    # Obtén el ID de la empresa seleccionada de la sesión
    company_id = request.session.get('selected_company_id')
    company = get_object_or_404(Company, id=company_id)

    #enlaza los position por area y empresa
    positions = Position.objects.filter(area=area, area__company=company)
    return render(request,'areas/area.html',{
        'area':area,
        'positions':positions
    })



@login_required(login_url="login")
def position(request, position_id):
    # Crea la página de cada puesto
    position = get_object_or_404(Position, id=position_id)

    # Si el usuario no es superusuario, asegúrate de que el puesto pertenece al usuario que ha iniciado sesión
    if not request.user.is_superuser and position.area.company.user != request.user:
        return HttpResponseForbidden("No tienes permiso para ver este puesto.")

    return render(request, 'positions/detail.html', {
        'position': position
    })

#muestra todos los puestos de la empresa seleccionada en el index
def company_positions(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    positions = Position.objects.filter(area__company=company)
    request.session['selected_company_id'] = company.id
    return render(request, 'positions/list.html', {
        'title': 'Puestos de Trabajo',
        'positions': positions
    })
@login_required(login_url="login")
def company_areas(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    areas = Area.objects.filter(company=company)
    request.session['selected_company_id'] = company.id
    return render(request, 'positions/list.html', {
        'title': 'Áreas',
        'areas': areas
    })



#eliminar empresa en index
@login_required
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company.delete()
    return redirect(reverse('index'))


#editar empresa en index
@login_required
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Empresa editada con éxito")
            return redirect('index')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'mainapp/edit_company.html', {'form': form})


#buscar
def search_company(request):
    query = request.GET.get('q')
    searched = False
    if query:
        companies = Company.objects.filter(name__icontains=query)
        searched = True
    else:
        companies = Company.objects.all()
    return render(request, 'mainapp/index.html', {'companies': companies, 'searched': searched})
