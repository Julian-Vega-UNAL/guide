# Generated by Django 4.0 on 2022-11-11 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Computadoras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='Sede_Centrel',
            new_name='Sede_central',
        ),
    ]
