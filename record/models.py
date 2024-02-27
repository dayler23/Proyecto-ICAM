from django.db import models

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

DEPARTMENT_CHOICES = [
    ('cochabamba', 'Cochabamba'),
    ('la_paz', 'La Paz'),
    ('santa_cruz', 'Santa Cruz'),
    ('tarija', 'Tarija'),
    ('oruro', 'Oruro'),
    ('beni', 'Beni'),
    ('pando', 'Pando'),
    ('tarija', 'Tarija'),
    ('potosi', 'Potosi'),
]
class Company(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre')
    address = models.CharField(max_length=300,verbose_name='Direccion')
    department = models.CharField(max_length=200,verbose_name='Departamento',choices=DEPARTMENT_CHOICES)
    sector = models.CharField(max_length=200, verbose_name='Sector')
    image = models.ImageField(default='null',verbose_name="Imagen",upload_to="companies")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

      
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    
    def __str__(self):
        return self.name
    

class Area(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre del Area')
    description = models.TextField(verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Editado el')

    #herencia una empresa N areas
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    class Meta:
        verbose_name='Area'
        verbose_name_plural='Areas'
    
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre del Puesto')
    activity_type = models.CharField(max_length=200,verbose_name='Tipo de Actividad')
    image = models.ImageField(default='null',verbose_name="Imagen",upload_to="positions")
    public=models.BooleanField(verbose_name="Publicado")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Editado el')
        
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


 
    class Meta:
        verbose_name='Puestos de Trabajo'
        verbose_name_plural='Puestos de Trabajo'
        ordering=['-created_at']
    
    def __str__(self):
        return self.name

