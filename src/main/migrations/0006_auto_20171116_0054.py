# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 17:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171116_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 19, 0, 54, 19, 854223)),
        ),
    ]
