from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#importar modelo para tener acceso a su atibutos
from.models import Page


# Create your views here.
@login_required(login_url="login")
def page(request,slug):

    page=Page.objects.get(slug=slug)

    return render(request,'pages/page.html',{
       'page': page
    })
