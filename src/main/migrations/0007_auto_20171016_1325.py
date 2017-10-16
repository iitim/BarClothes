# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 06:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171009_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 13, 25, 25, 615826)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('wpy', 'wait_for_pay'), ('wac', 'wait_for_admin_confirm'), ('wss', 'wait_for_seller_sent'), ('suc', 'success'), ('cnp', 'customer_not_pay'), ('cpe', 'customer_pay_error'), ('ccl', 'customer_cancel'), ('sns', 'seller_not_sent_product')], default='wpy', max_length=3),
        ),
        migrations.AlterField(
            model_name='transactionlog',
            name='status',
            field=models.CharField(choices=[('wpy', 'wait_for_pay'), ('wac', 'wait_for_admin_confirm'), ('wss', 'wait_for_seller_sent'), ('suc', 'success'), ('cnp', 'customer_not_pay'), ('cpe', 'customer_pay_error'), ('ccl', 'customer_cancel'), ('sns', 'seller_not_sent_product')], default='suc', max_length=3),
        ),
    ]
