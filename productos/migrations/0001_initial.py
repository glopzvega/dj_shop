# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('precio', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
    ]