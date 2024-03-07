from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from record.models import User,Company, Area  # Importa los modelos de la empresa y el área
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Create your views here.
from django.db.models import Count
from django.db.models.functions import Lower

@login_required
def index(request):
    companies = None  # Inicializa la variable companies

    if request.user.is_superuser:
        companies = Company.objects.annotate(area_count=Count('area')).order_by(Lower('name')) # Si es superusuario, obtiene todas las empresas y las ordena por nombre
    else:
        companies = Company.objects.filter(user=request.user).annotate(area_count=Count('area')).order_by(Lower('name'))

    if not companies.exists():  # Verifica si la consulta devolvió algún resultado
        messages.warning(request, "No hay empresas disponibles")
    return render(request, 'mainapp/index.html', {'companies': companies})

#registro
def register_page(request):
     if request.user.is_authenticated:
          return redirect('inicio')
     else:
          register_form=RegisterForm()

          if request.method=='POST':
               register_form=RegisterForm(request.POST)

               if register_form.is_valid():
                    register_form.save()
                    messages.success(request,"Registro Exitoso")

                    return redirect('inicio')
          
          return render(request,'users/register.html',{
                    'title':'Registro',
                    'register_form':register_form
     })

##login
def login_page(request):
     if request.user.is_authenticated:
          return redirect('inicio')
     else:
          if request.method=='POST':
               username=request.POST.get("username")
               password=request.POST.get("password")

               user=authenticate(request,username=username,password=password)

               if user is not None:
                    login(request,user)
                    return redirect('inicio')
               else:
                    messages.warning(request,"No te has identificado correctamente")

          return render(request,'users/login.html',{
               'title':'Identificate',
                    
          })

def logout_user(request):
     logout(request)
     return redirect('login')



@login_required
def profile(request):
    users = User.objects.none()  # Inicializa la variable users

    if request.user.is_superuser:
        users = User.objects.all()  # Recupera todos los usuarios si es superusuario
    else:
        users = User.objects.filter(id=request.user.id)  # Recupera solo el usuario actual si no es superusuario

    return render(request, 'users/profile.html', {'users': users})


#delete user
@login_required
def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('inicio')  # Redirige a los usuarios no superusuarios a la página de inicio

    user_to_delete = User.objects.get(id=user_id)
    user_to_delete.delete()
    messages.success(request, "Usuario eliminado con éxito")
    return redirect('profile')

@login_required
def toggle_superuser(request, user_id):
    if not request.user.is_superuser:
        return redirect('inicio')  # Solo permite que el superusuario cambie el estado de superusuario de otros usuarios

    user = User.objects.get(id=user_id)
    user.is_superuser = not user.is_superuser  # Cambia el estado de superusuario
    user.save()

    if user.is_superuser:
        messages.success(request, f"{user.username} ahora es superusuario.")
    else:
        messages.success(request, f"{user.username} ya no es superusuario.")

    return redirect('profile')





