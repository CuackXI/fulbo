# Generated by Django 5.0.6 on 2024-05-16 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0005_rename_idapipais_competiciones_pais_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competiciones',
            name='Temporada',
        ),
    ]
