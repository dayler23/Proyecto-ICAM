# Create your models here.
from django.db import models
from record.models import Position  # Make sure to import the Position model

class LightingEvaluation(models.Model):
    PERIOD_CHOICES = [
        ('Dia', 'Dia'),
        ('Noche', 'Noche'),
    ]
    TYPE_CHOICES = [
        ('Natural', 'Natural'),
        ('Artificial', 'Artificial'),
        ('Mixta', 'Mixta'),
    ]
    PARAMETER_CHOICES=[
        (50, '50'),
        (100, '100'),
        (300, '300'),
        (750, '750'),
        (3000, '3000+'),
    ]

    period = models.CharField(max_length=5, choices=PERIOD_CHOICES, verbose_name='Periodo')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Tipo de Iluminación')    
    time = models.TimeField(verbose_name='Hora')

    left_1 = models.FloatField(null=True, blank=True, verbose_name='Izq1')
    left_2 = models.FloatField(null=True, blank=True, verbose_name='Izq2')
    left_3 = models.FloatField(null=True, blank=True, verbose_name='Izq3')
    left_4 = models.FloatField(null=True, blank=True, verbose_name='Izq4')
    left_5 = models.FloatField(null=True, blank=True, verbose_name='Izq5')

    center_1 = models.FloatField(null=True, blank=True, verbose_name='Cen1')
    center_2 = models.FloatField(null=True, blank=True, verbose_name='Cen2')
    center_3 = models.FloatField(null=True, blank=True, verbose_name='Cen3')
    center_4 = models.FloatField(null=True, blank=True, verbose_name='Cen4')
    center_5 = models.FloatField(null=True, blank=True, verbose_name='Cen5')
        
    right_1 = models.FloatField(null=True, blank=True, verbose_name='Der1')
    right_2 = models.FloatField(null=True, blank=True, verbose_name='Der2')
    right_3 = models.FloatField(null=True, blank=True, verbose_name='Der3')
    right_4 = models.FloatField(null=True, blank=True, verbose_name='Der4')
    right_5 = models.FloatField(null=True, blank=True, verbose_name='Der5')
 
    average = models.FloatField(verbose_name='Promedio')
    maximum = models.FloatField(verbose_name='Máximo')
    minimum = models.FloatField(verbose_name='Mínimo')

    parameter = models.IntegerField(choices=PARAMETER_CHOICES, verbose_name='Parámetro')
    date = models.DateField(verbose_name='Fecha')


    observations = models.TextField(null=True, blank=True, verbose_name='Observaciones')
    suggestions = models.TextField(null=True, blank=True, verbose_name='Sugerencias')

    # Here is the relationship with the Position model
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posición')
