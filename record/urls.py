from django.urls import path
from . import views


urlpatterns = [
    path('puestos/',views.list,name="list_positions"),
    path('area/<int:area_id>',views.area,name="area"),
    path('puesto/<int:position_id>',views.position,name="position"),
    path('eliminar-empresa/<int:company_id>/', views.delete_company, name='delete_company'),
    path('editar-empresa/<int:company_id>/', views.edit_company, name='edit_company'),
    path('search/', views.search_company, name='search_company'),

    path('empresa/<int:company_id>/areas', views.company_areas, name='company_areas'),

    path('añadir-area/', views.add_area, name='add_area'),
    path('eliminar-area/<int:area_id>/', views.delete_area, name='delete_area'),
    path('editar-area/<int:area_id>/', views.edit_area, name='edit_area'),
    path('search-area/', views.search_area, name='search_area'),
    path('search-area/<int:company_id>/', views.search_area, name='search_area_company'),
]


