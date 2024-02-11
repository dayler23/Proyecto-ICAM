from django.urls import path
from . import views


urlpatterns = [
    path('puestos/',views.list,name="list_positions"),
    path('area/<int:area_id>',views.area,name="area"),
    path('puesto/<int:position_id>',views.position,name="position"),
    path('empresa/<int:company_id>/puestos', views.company_positions, name='company_positions'),
    path('eliminar-empresa/<int:company_id>/', views.delete_company, name='delete_company'),
    path('editar-empresa/<int:company_id>/', views.edit_company, name='edit_company'),

]


