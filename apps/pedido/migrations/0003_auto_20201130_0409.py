# Generated by Django 3.0 on 2020-11-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_auto_20201130_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(blank=True, related_name='pedidos_tiene', to='pedido.producto'),
        ),
    ]
