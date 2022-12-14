# Generated by Django 4.0 on 2022-11-11 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('Id_empresa', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_empresa', models.CharField(max_length=50)),
                ('Sede_Centrel', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=20)),
                ('Sitio_web', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('Id_procesador', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_procesador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Computadoras',
            fields=[
                ('Id_computadora', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre_computadora', models.CharField(max_length=50)),
                ('Medidas', models.DecimalField(decimal_places=2, max_digits=3)),
                ('RAM', models.IntegerField()),
                ('Disco_solido', models.IntegerField()),
                ('Color', models.CharField(max_length=30)),
                ('Unidades_disponibles', models.IntegerField()),
                ('Empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Computadoras.empresa')),
                ('Procesador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Computadoras.procesador')),
            ],
        ),
    ]
