from django.contrib.auth.models import User
from record.models import Company, Area, Position

def get_areas(request):
    if request.user.is_authenticated:
        # Obtén la empresa del usuario que ha iniciado sesión
        companies = Company.objects.filter(user=request.user)

        # Obtén solo las áreas de esa empresa
        areas = Area.objects.filter(company__in=companies).values_list('id', 'name')

        return {
            'areas': areas,
        }
    else:
        return {
            'areas': [],
        }

