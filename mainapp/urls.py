from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('inicio/',views.index,name="inicio"), 

    path('registro/',views.register_page,name="register"), 
    path('login/',views.login_page,name="login"), 

    path('logout/',views.logout_user,name="logout"), 
    path('eliminar-empresa/<int:company_id>/', views.delete_company, name='delete_company'),


]


