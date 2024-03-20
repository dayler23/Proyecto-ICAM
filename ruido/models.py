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
    min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Mínimo')
    max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Maximo')
    parameter = models.DecimalField(max_digits=3, blank=True, verbose_name='LEP(*)')
    average = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='LAeqT')

    exposure_time = models.DurationField(null=True, blank=True, verbose_name='TMPE')

    min_exposure_time = models.DurationField(null=True, blank=True, verbose_name='TPE')
    dose = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Dosis')
    method = models.CharField(max_length=100, default='Medición del Nivel de Presión Acustica Continuo Equivalente Ponderado A', verbose_name='Metodo')
    
    # 25 variables de tipo decimal para mediciones de ruido
    m_1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Medición 1')
    m_2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Medición 2')
    m_3 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_4 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_5 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_6 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_7 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_8 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_9 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_10 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_11 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_12 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_13 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_14 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_15 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_16 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_17 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_18 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_19 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_20= models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_21= models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_22 = models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_23 = models.DecimalField(null=True, blank=True, verbose_name='Medición 2')
    m_24= models.DecimalField(null=True, blank=True, verbose_name='Medición 1')
    m_25= models.DecimalField(null=True, blank=True, verbose_name='Medición 1')

    observations = models.TextField(null=True, blank=True, verbose_name='Observaciones')
    suggestions = models.TextField(null=True, blank=True, verbose_name='Sugerencias')

    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posición')
