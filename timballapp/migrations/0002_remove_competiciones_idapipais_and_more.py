# Generated by Django 5.0.6 on 2024-05-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competiciones',
            name='IdApiPais',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='IdApiPais',
        ),
        migrations.AddField(
            model_name='competiciones',
            name='Pais',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='Pais',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
