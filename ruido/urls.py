from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion_ruido/<int:position_id>/', views.evaluacion_ruido, name='evaluacion_ruido'),
    # otras rutas...
]
