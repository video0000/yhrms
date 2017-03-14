# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_auto_20170206_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalleave',
            name='reason',
            field=models.TextField(null=True, verbose_name='\u4f11\u5047\u539f\u56e0', blank=1),
        ),
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.TextField(null=True, verbose_name='\u4f11\u5047\u539f\u56e0', blank=1),
        ),
    ]
