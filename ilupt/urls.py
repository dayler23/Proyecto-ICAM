from django.urls import path
from . import views


urlpatterns = [
   path('evaluacion_iluminacion/<int:position_id>/', views.evaluacion_iluminacion, name='evaluacion_iluminacion'),
]


