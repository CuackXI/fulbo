# Generated by Django 5.0.6 on 2024-05-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0022_alter_apuesta_p_idapibookmaker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta_p',
            name='Tipo',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
