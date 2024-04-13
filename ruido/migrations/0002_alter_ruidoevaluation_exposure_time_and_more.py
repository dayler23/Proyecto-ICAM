# Generated by Django 5.0 on 2024-04-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruidoevaluation',
            name='exposure_time',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='TMPE (horas)'),
        ),
        migrations.AlterField(
            model_name='ruidoevaluation',
            name='parameter',
            field=models.DecimalField(decimal_places=2, default=85.0, max_digits=6, verbose_name='LEP(*)'),
        ),
    ]