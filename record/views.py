from django.shortcuts import render,get_object_or_404

#IMPORTACION DE MODELOS PARA OBTENER DATOS
from record.models import Company,Area,Position

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden





# Create your views here.

#metodo para extraer todo el objeto de Position y mostrar en list.html
@login_required(login_url="login")
def list(request):
    # Obtén solo las empresas del usuario que ha iniciado sesión
    companies = Company.objects.filter(user=request.user)

    # Obtén solo las áreas de esas empresas
    areas = Area.objects.filter(company__in=companies)

    # Obtén solo los puestos de trabajo de esas áreas
    positions = Position.objects.filter(area__in=areas)

    paginator = Paginator(positions, 4)
    page = request.GET.get('page')
    page_positions = paginator.get_page(page)

    return render(request, 'positions/list.html', {
        'title': 'Puestos de Trabajo',
        'positions': page_positions
    })



#metodo para extraer todo el objeto de area y mostrar los 
#positions de cada area

#muestra los puestos por area al seleccionar el area 
@login_required(login_url="login")
def area(request,area_id):

    #crea pagina de cada area
    area=get_object_or_404(Area,id=area_id)

    #enlaza los position por area
    positions = Position.objects.filter(area=area)
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





