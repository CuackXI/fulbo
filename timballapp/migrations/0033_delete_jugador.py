# Generated by Django 5.0.6 on 2024-06-07 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0032_alter_jugador_altura_alter_jugador_edad_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jugador',
        ),
    ]