# Generated by Django 5.0.6 on 2024-09-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timballapp', '0039_statsequipo_statsjugador'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StatsJugador',
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='Amarillas',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='DiferenciaGoles',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesContra',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesContraLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesContraVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesFavor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesFavorLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='GolesFavorVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosEmpatados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosEmpatadosLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosEmpatadosVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosGanados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosGanadosLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosGanadosVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosJugados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosPerdidos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosPerdidosLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PartidosPerdidosVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='Penales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='Puntos',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PuntosLocal',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='PuntosVisitante',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='Rojas',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='SinGoles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='SinGolesLocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsequipo',
            name='SinGolesVisitante',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statsequipo',
            name='IdApiEquipo_id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
