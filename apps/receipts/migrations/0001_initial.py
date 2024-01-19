# Generated by Django 5.0.1 on 2024-01-19 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer', models.CharField(max_length=250)),
                ('purchaseDate', models.DateField()),
                ('purchaseTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortDescription', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.receipt')),
            ],
        ),
    ]