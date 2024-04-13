from django.db import models
from record.models import Position  # Asegúrate de importar el modelo Position si es necesario

class RuidoEvaluation(models.Model):
   
    TYPE_CHOICES = [
        ('Estable', 'Estable'),
        ('Periodico', 'Tráfico'),
        ('Aletorio', 'Industrial'),
        ('Impacto', 'Impacto'),
    ]
    ANALYSIS_CHOICES = [
        ('Fija', 'Fija'),
        ('Movil', 'Movil'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Tipo de Ruido')
    source_type = models.CharField(max_length=10, choices=ANALYSIS_CHOICES, verbose_name='Tipo de Fuente')    
    date = models.DateField(verbose_name='Fecha')

    # Campos específicos para la evaluación del ruido
    min = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Mínimo')
    max = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Maximo')
    parameter = models.DecimalField(max_digits=6, decimal_places=2, default=85.00, verbose_name='LEP(*)')
    average = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='LAeqT')

    exposure_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='TMPE (horas)')

    min_exposure_time = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='TPE (horas)')
    dose = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Dosis')
    method = models.CharField(max_length=100, default='Medición del Nivel de Presión Acustica Continuo Equivalente Ponderado A', verbose_name='Metodo')
    
    # 25 variables de tipo decimal para mediciones de ruido
    m_1 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 1')
    m_2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 2')
    m_3 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 3')
    m_4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 4')
    m_5 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 5')
    m_6 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 6')
    m_7 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 7')
    m_8 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 8')
    m_9 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 9')
    m_10 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 10')
    m_11 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 11')
    m_12 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 12')
    m_13 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 13')
    m_14 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 14')
    m_15 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 15')
    m_16 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 16')
    m_17 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 17')
    m_18 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 18')
    m_19 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 19')
    m_20 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 20')
    m_21 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 21')
    m_22 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 22')
    m_23 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 23')
    m_24 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 24')
    m_25 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='Medición 25')

    observations = models.TextField(null=True, blank=True, verbose_name='Observaciones')
    suggestions = models.TextField(null=True, blank=True, verbose_name='Sugerencias')

    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posición')
