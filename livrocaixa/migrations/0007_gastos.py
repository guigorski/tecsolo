# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-10 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livrocaixa', '0006_auto_20161214_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]