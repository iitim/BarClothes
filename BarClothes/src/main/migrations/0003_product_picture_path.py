# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170928_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture_path',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
