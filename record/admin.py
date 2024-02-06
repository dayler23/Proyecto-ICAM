from django.contrib import admin

# Register your models here.
from typing import Any
from django.contrib import admin
from .models import Company,Area,Position
from .forms import PositionForm
from django.utils.html import format_html

   
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    list_display=('name','user','department','address','created_at',)
    search_fields=('name',)

    #GUARDAR EL ID DEL USUARIO al momento de crear una empresa
    """def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id=request.user.id

        obj.save()"""


class AreaAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    list_display=('name', 'get_company_name', 'get_company_department', 'get_company_address')
    search_fields=('name', 'description', 'company__name', 'company__department', 'company__address')

    def get_company_name(self, obj):
        return obj.company.name

    get_company_name.short_description = 'Empresa'
    get_company_name.admin_order_field = 'company__name'  # Permite ordenar por nombre de compañía

    def get_company_department(self, obj):
        return obj.company.department

    get_company_department.short_description = 'Departamento'
    get_company_department.admin_order_field = 'company__department'  # Permite ordenar por departamento de la compañía

    def get_company_address(self, obj):
        return obj.company.address

    get_company_address.short_description = 'Dirección'
    get_company_address.admin_order_field = 'company__address'  # Permite ordenar por dirección de la compañía



####################################
  
    
class PositionAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    form = PositionForm
    raw_id_fields = ('area',)  
    
    list_display = ('name', 'get_area_name', 'get_company_name', 'public','evaluate')
    search_fields = ['name', 'area__name', 'area__company__name'] 
    
    def get_area_name(self, obj):
        return obj.area.name

    get_area_name.short_description = 'Área'
    get_area_name.admin_order_field = 'area__name'  # Permite ordenar por nombre de área

    def get_company_name(self, obj):
        return obj.area.company.name

    get_company_name.short_description = 'Empresa'
    get_company_name.admin_order_field = 'area__company__name'  # Permite ordenar por nombre de compañía

    search_fields = ['name', 'area__name', 'area__company__name']  # Búsqueda por nombre de puesto, nombre de área y nombre de compañía

      #botono de evaluacion 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'area' and 'company' in request.GET:
            company_id = request.GET['company']
            kwargs["queryset"] = Area.objects.filter(company_id=company_id)
        return super(PositionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_evaluate_button'] = True
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def evaluate(self, obj):
        buttons = ['ILU', 'RUI','ven', 'est','vib', 'pst']
        html = ''
        for button in buttons:
            html += format_html('<a class="button" href="/evaluate/{}/{}">{}</a> ', obj.id, button, button.upper())
        return format_html(html)

    evaluate.short_description = 'Evaluar'
    evaluate.allow_tags = True


# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Position,PositionAdmin)


