# Generated by Django 4.2.6 on 2023-10-18 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del Usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password_usuario',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Password del Usuario'),
        ),
    ]
