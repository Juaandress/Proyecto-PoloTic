# Generated by Django 3.0 on 2020-11-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_medico',
            name='medico',
            field=models.ManyToManyField(blank=True, related_name='modifica', to='user.medico'),
        ),
    ]
