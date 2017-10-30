# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171009_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttotag',
            name='product',
        ),
        migrations.RemoveField(
            model_name='producttotag',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
        ),
        migrations.DeleteModel(
            name='ProductToTag',
        ),
    ]
