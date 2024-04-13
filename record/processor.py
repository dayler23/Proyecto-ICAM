from django.contrib.auth.models import User
from record.models import Company, Area, Position

def get_areas(request):
    if request.user.is_authenticated and 'selected_company_id' in request.session:
        try:
            company = Company.objects.get(id=request.session['selected_company_id'])
            areas = Area.objects.filter(company=company).values_list('id', 'name')
            return {
                'areas': areas,
                'selected_company_id': request.session['selected_company_id'],
                'selected_area_id': request.session.get('selected_area_id', None)  # Agrega esta línea
            }
        except Company.DoesNotExist:
            return {
                'areas': [],
            }
    else:
        return {
            'areas': [],
        }
