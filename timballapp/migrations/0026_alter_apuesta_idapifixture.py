# Generated by Django 5.0.6 on 2024-05-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0025_apuesta_porcentaje_delete_apuesta_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuesta',
            name='IdApiFixture',
            field=models.IntegerField(),
        ),
    ]