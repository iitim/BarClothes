# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-11-19 18:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 1, 15, 17, 90901)),
        ),
    ]
