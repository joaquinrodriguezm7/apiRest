# Generated by Django 4.2.2 on 2023-12-01 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_viaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
    ]
