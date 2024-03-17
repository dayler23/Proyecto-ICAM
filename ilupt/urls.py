from django.urls import path
from . import views


urlpatterns = [
   path('evaluacion_iluminacion/<int:position_id>/', views.evaluacion_iluminacion, name='evaluacion_iluminacion'),
   
path('graph_day/<int:position_id>/', views.graph_day, name='graph_day'),
    path('graph_night/<int:position_id>/', views.graph_night, name='graph_night'),
]


