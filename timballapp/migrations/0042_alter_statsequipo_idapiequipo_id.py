# Generated by Django 5.0.6 on 2024-09-24 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0041_alter_statsequipo_idapiequipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statsequipo',
            name='IdApiEquipo_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='timballapp.equipo'),
        ),
    ]
