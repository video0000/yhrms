# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_auto_20170111_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalworkexperience',
            name='transfer_order_number',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8c03\u4ee4\u7f16\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='transfer_order_number',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8c03\u4ee4\u7f16\u53f7', blank=True),
        ),
    ]
