from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('inicio/',views.index,name="inicio"), 

    path('registro/',views.register_page,name="register"), 
    path('login/',views.login_page,name="login"), 

    path('logout/',views.logout_user,name="logout"), 

    path('profile/', views.profile, name='profile'),
    
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]


