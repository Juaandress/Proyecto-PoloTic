# Generated by Django 3.1.3 on 2020-12-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20201130_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
