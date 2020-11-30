# Generated by Django 3.0 on 2020-11-30 05:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_paciente', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='historial_medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha', models.DateField(blank=True, default=datetime.date.today)),
                ('medico', models.ManyToManyField(related_name='modifica', to='user.medico')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]
