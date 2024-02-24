from django.shortcuts import render,get_object_or_404,redirect

#IMPORTACION DE MODELOS PARA OBTENER DATOS
from record.models import Company,Area,Position

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from record.forms import AreaForm  # Importa el formulario de área
from mainapp.forms import CompanyForm
from .forms import PositionForm
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


@login_required(login_url="login")
def company_areas(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    areas = Area.objects.filter(company=company)
    request.session['selected_company_id'] = company.id
    return render(request, 'positions/list.html', {
        'title': 'ÁREAS',
        'areas': areas,
        'company': company  # Pasa el objeto company a la plantilla
        
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


#buscar empresa
def search_company(request):
    query = request.GET.get('q')
    searched = False
    if query:
        companies = Company.objects.filter(name__icontains=query)
        searched = True
    else:
        companies = Company.objects.all()
    return render(request, 'mainapp/index.html', {'companies': companies, 'searched': searched})

#añadir area
@login_required(login_url="login")
def add_area(request):
    if request.method == 'POST':
        # Obtén el ID de la empresa seleccionada de la sesión
        selected_company_id = request.session.get('selected_company_id')

        # Si no hay ninguna empresa seleccionada, muestra un mensaje de error
        if selected_company_id is None:
            messages.error(request, "Por favor, selecciona una empresa primero.")
            return redirect('index')

        # Obtén la empresa seleccionada
        selected_company = get_object_or_404(Company, id=selected_company_id)

        # Crea una nueva área con los datos del formulario
        new_area = Area(name=request.POST['name'], description=request.POST['description'], company=selected_company)
        new_area.save()

        messages.success(request, "Área añadida con éxito")
        return redirect('company_areas', company_id=selected_company_id)

#eliminar area
@login_required(login_url="login")
def delete_area(request, area_id):
    # Obtén el área que se va a eliminar
    area = get_object_or_404(Area, id=area_id)

    # Verifica que el usuario tenga permiso para eliminar el área
    if request.user.is_superuser:
        # Guarda el ID de la empresa antes de eliminar el área
        company_id = area.company.id
        area.delete()
        messages.success(request, "Área eliminada con éxito")
        # Redirige al usuario a la lista de áreas de la empresa
        return redirect('company_areas', company_id=company_id)
    else:
        messages.error(request, "No tienes permiso para eliminar esta área")
        return redirect('index')
    
#edit area
@login_required(login_url="login")
def edit_area(request, area_id):
    # Obtén el área que se va a editar
    area = get_object_or_404(Area, id=area_id)

    if request.method == 'POST':
        # Actualiza los datos del área con los datos del formulario
        area.name = request.POST['name']
        area.description = request.POST['description']
        area.save()

        messages.success(request, "Área editada con éxito")
        return redirect('company_areas', company_id=area.company.id)

    # Si la solicitud no es un POST, muestra la página de edición con el formulario
    return render(request, 'edit_area.html', {'area': area})

#buscar area
def search_area(request):
    query = request.GET.get('q')
    searched = False
    if query:
        areas = Area.objects.filter(name__icontains=query)
        searched = True
    else:
        areas = Area.objects.all()

    # Asegúrate de que cada área tiene un company_id válido.
    for area in areas:
        if not area.company_id:
            raise ValueError(f"Area {area.id} does not have a valid company_id.")

    return render(request, 'positions/list.html', {'title':'AREAS','areas': areas, 'searched': searched})

#añadir puesto
@login_required(login_url="login")
def add_position(request, area_id):
    # Obtén el área que se ha seleccionado previamente
    area = get_object_or_404(Area, id=area_id)

    if request.method == 'POST':
        form = PositionForm(request.POST, request.FILES)
        if form.is_valid():
            # Crea un nuevo puesto con los datos del formulario y el área seleccionada
            new_position = form.save(commit=False)
            new_position.area = area
            new_position.save()

            messages.success(request, "Puesto añadido con éxito")
            return redirect('area', area_id=area_id)
    else:
        form = PositionForm()

    return render(request, 'add_position.html', {'form': form})

#DELETE POSITION
@login_required(login_url="login")
def delete_position(request, area_id, position_id):
    # Obtén el puesto que se va a eliminar
    position = get_object_or_404(Position, id=position_id)

    # Verifica que el usuario tenga permiso para eliminar el puesto
    if request.user.is_superuser or request.user == position.area.company.user:
        position.delete()
        messages.success(request, "Puesto eliminado con éxito")
        # Redirige al usuario a la lista de puestos de la área
        return redirect('area', area_id=area_id)
    else:
        messages.error(request, "No tienes permiso para eliminar este puesto")
        return redirect('index')
#edit position 
@login_required(login_url="login")
def edit_position(request, area_id, position_id):
    # Obtén el puesto que se va a editar
    position = get_object_or_404(Position, id=position_id)

    # Verifica que el usuario tenga permiso para editar el puesto
    if request.user.is_superuser or request.user == position.area.company.user:
        if request.method == 'POST':
            form = PositionForm(request.POST, request.FILES, instance=position)
            if form.is_valid():
                form.save()
                messages.success(request, "Puesto editado con éxito")
                # Redirige al usuario a la lista de puestos de la área
                return redirect('area', area_id=position.area.id)
        else:
            form = PositionForm(instance=position)
    else:
        messages.error(request, "No tienes permiso para editar este puesto")
        return redirect('index')

    return render(request, 'edit_position.html', {'form': form})
#buscar puesto:
from django.db.models import Q

def search_position(request, area_id):
    query = request.GET.get('q')
    searched = False
    area = Area.objects.get(id=area_id)
    if query:
        positions = Position.objects.filter(Q(name__istartswith=query), area_id=area.id)
        searched = True
    else:
        positions = Position.objects.filter(area_id=area.id)

    return render(request, 'areas/area.html', {'positions': positions, 'area': area, 'searched': searched})


