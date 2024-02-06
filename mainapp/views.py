from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from record.models import Company, Area  # Importa los modelos de la empresa y el área

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # Obtén las empresas del usuario actual
        companies = Company.objects.filter(user=request.user)
    else:
        # Si el usuario no está autenticado, no hay empresas para mostrar
        companies = None

    return render(request,'mainapp/index.html',{
        'title':'Inicio',
        'companies': companies,
    })



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
