# Generated by Django 4.2.2 on 2023-12-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='patente',
            field=models.CharField(db_column='Patente', max_length=9, primary_key=True, serialize=False, verbose_name='Patente del Vehiculo'),
        ),
    ]
