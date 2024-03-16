# Generated by Django 5.0 on 2024-03-12 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('record', '0002_alter_company_user_alter_position_activity_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightingEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('Dia', 'Dia'), ('Noche', 'Noche')], max_length=5, verbose_name='Periodo')),
                ('type', models.CharField(choices=[('Natural', 'Natural'), ('Artificial', 'Artificial'), ('Mixta', 'Mixta')], max_length=10, verbose_name='Tipo de Iluminación')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('left_1', models.FloatField(blank=True, null=True, verbose_name='Izq1')),
                ('left_2', models.FloatField(blank=True, null=True, verbose_name='Izq2')),
                ('left_3', models.FloatField(blank=True, null=True, verbose_name='Izq3')),
                ('left_4', models.FloatField(blank=True, null=True, verbose_name='Izq4')),
                ('left_5', models.FloatField(blank=True, null=True, verbose_name='Izq5')),
                ('center_1', models.FloatField(blank=True, null=True, verbose_name='Cen1')),
                ('center_2', models.FloatField(blank=True, null=True, verbose_name='Cen2')),
                ('center_3', models.FloatField(blank=True, null=True, verbose_name='Cen3')),
                ('center_4', models.FloatField(blank=True, null=True, verbose_name='Cen4')),
                ('center_5', models.FloatField(blank=True, null=True, verbose_name='Cen5')),
                ('right_1', models.FloatField(blank=True, null=True, verbose_name='Der1')),
                ('right_2', models.FloatField(blank=True, null=True, verbose_name='Der2')),
                ('right_3', models.FloatField(blank=True, null=True, verbose_name='Der3')),
                ('right_4', models.FloatField(blank=True, null=True, verbose_name='Der4')),
                ('right_5', models.FloatField(blank=True, null=True, verbose_name='Der5')),
                ('average', models.FloatField(verbose_name='Promedio')),
                ('maximum', models.FloatField(verbose_name='Máximo')),
                ('minimum', models.FloatField(verbose_name='Mínimo')),
                ('parameter', models.IntegerField(choices=[('50', '50'), ('100', '100'), ('300', '300'), ('750', '750'), ('3000+', '3000')], verbose_name='Parámetro')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('suggestions', models.TextField(blank=True, null=True, verbose_name='Sugerencias')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.position', verbose_name='Posición')),
            ],
        ),
    ]
