# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 08:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171106_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 15, 33, 30, 198758)),
        ),
        migrations.AlterField(
            model_name='userextenddata',
            name='bank_account',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]