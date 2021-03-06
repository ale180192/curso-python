# Generated by Django 3.2.6 on 2021-08-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField()),
                ('impuestos', models.FloatField()),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=36)),
                ('stock', models.PositiveSmallIntegerField()),
                ('costo_unitario', models.FloatField()),
            ],
        ),
    ]
