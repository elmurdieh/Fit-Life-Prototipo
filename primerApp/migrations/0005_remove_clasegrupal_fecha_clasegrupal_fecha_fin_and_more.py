# Generated by Django 5.1.1 on 2024-11-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerApp', '0004_clasegrupal_imgreferencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clasegrupal',
            name='fecha',
        ),
        migrations.AddField(
            model_name='clasegrupal',
            name='fecha_Fin',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='clasegrupal',
            name='fecha_Inicio',
            field=models.DateField(default='2024-01-01'),
        ),
    ]