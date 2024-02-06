from django.urls import path
from . import views


urlpatterns = [
    path('puestos/',views.list,name="list_positions"),
    path('area/<int:area_id>',views.area,name="area"),
    path('puesto/<int:position_id>',views.position,name="position"),
   
]


