from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from record.models import Company ,Area

#formulario de registro
class RegisterForm(UserCreationForm):
    class Meta:
        model=User

        fields=['username','email','first_name','last_name','password1','password2']

#formulario para agregar empresa
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'  # Todos los campos del modelo Company
        labels={
            'name':'Empresa:',
            'sector':'Sector o Rubro',
            'image':'Logo',
            'user':'Usuario Encargado'
        }

