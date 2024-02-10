from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from record.models import Company, Area  # Importa los modelos de la empresa y el área
from django.contrib.auth.decorators import login_required
from mainapp.forms import CompanyForm

# Create your views here.
@login_required
def index(request):
    form = None  # Inicializa la variable form
    companies = None  # Inicializa la variable companies
    if request.user.is_superuser:
        companies = Company.objects.all()
        if not companies.exists():  # Verifica si la consulta devolvió algún resultado
            messages.warning(request, "No hay empresas disponibles")
        else:
            if request.method == 'POST':
                form = CompanyForm(request.POST, request.FILES)  # Añade request.FILES
                if form.is_valid():
                    form.save()
                    messages.success(request, "Empresa añadida con éxito")
                    return redirect('index')  # Redirige a la misma página después de guardar
            else:
                form = CompanyForm()  # Instancia el formulario
    else:
        companies = Company.objects.filter(user=request.user)
        if not companies.exists():  # Verifica si la consulta devolvió algún resultado
            messages.warning(request, "No tienes ninguna empresa asociada")

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        'companies': companies,
        'form': form,  # Pasa el formulario al contexto
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

#buscar empresa en index
