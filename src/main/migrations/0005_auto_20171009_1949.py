# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171009_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='main.Tag'),
        ),
    ]
