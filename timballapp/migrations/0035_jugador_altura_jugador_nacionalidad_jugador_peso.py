# Generated by Django 5.0.6 on 2024-06-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0034_jugador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='Altura',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='Nacionalidad',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='Peso',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
