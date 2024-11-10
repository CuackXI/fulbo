# Generated by Django 5.0.6 on 2024-05-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0024_alter_apuesta_p_porcentaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='Porcentaje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Apuesta_P',
        ),
    ]