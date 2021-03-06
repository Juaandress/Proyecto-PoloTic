# Generated by Django 3.0 on 2020-11-30 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('clasificacion', models.CharField(max_length=60)),
                ('distancia', models.CharField(blank=True, choices=[('L', 'Lejos'), ('C', 'Cerca')], max_length=2, null=True)),
                ('lado', models.CharField(blank=True, choices=[('I', 'Izquierda'), ('D', 'Derecha')], max_length=2, null=True)),
                ('armazon', models.BooleanField(blank=True, default=False, null=True)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField(blank=True, null=True)),
                ('subtotal', models.FloatField()),
                ('tipo_pago', models.CharField(max_length=30)),
                ('Finalizado', models.BooleanField(default=False)),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.paciente')),
                ('productos', models.ManyToManyField(related_name='pedidos_tiene', to='pedido.producto')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tecnico')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.vendedor')),
            ],
        ),
    ]
