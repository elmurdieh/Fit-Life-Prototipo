# Generated by Django 5.1.1 on 2024-11-22 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primerApp', '0008_alter_clasegrupal_entrenador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clasegrupal',
            old_name='imgReferencia',
            new_name='imgCG',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='imgPro',
        ),
    ]
