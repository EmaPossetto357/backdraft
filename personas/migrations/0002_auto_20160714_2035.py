# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-14 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fallecido',
            name='persona',
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_desceso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Fallecimiento'),
        ),
        migrations.DeleteModel(
            name='Fallecido',
        ),
    ]
