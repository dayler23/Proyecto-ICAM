# Generated by Django 5.0 on 2024-03-09 01:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='position',
            name='activity_type',
            field=models.CharField(max_length=200, verbose_name='Tipo de Actividad'),
        ),
        migrations.AlterField(
            model_name='position',
            name='image',
            field=models.ImageField(default='null', upload_to='positions', verbose_name='Imagen'),
        ),
    ]
