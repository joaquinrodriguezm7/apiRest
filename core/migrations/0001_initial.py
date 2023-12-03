# Generated by Django 4.2.2 on 2023-12-02 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id_tipousuario', models.AutoField(db_column='Id_Tipo_Usuario', primary_key=True, serialize=False, verbose_name='Id Tipo Usuario')),
                ('tipoUsuario', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='id_usuario')),
                ('nombre_usuario', models.CharField(max_length=50, unique=True, verbose_name='Nombre del Usuario')),
                ('password_usuario', models.CharField(max_length=50, verbose_name='Password del Usuario')),
                ('tipoUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Patente del Vehiculo')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca del Vehiculo')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo  del Vehiculo')),
                ('capacidad', models.IntegerField(blank=True, null=True)),
                ('nombre_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuario', to_field='nombre_usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id_viaje', models.AutoField(primary_key=True, serialize=False, verbose_name='id_viaje')),
                ('inicio', models.CharField(blank=True, max_length=50, null=True)),
                ('termino', models.CharField(blank=True, max_length=50, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('nombre_usuario_cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre_usuario_dueño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
                ('patente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo')),
            ],
        ),
    ]
