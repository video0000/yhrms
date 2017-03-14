# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20170104_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduction',
            name='degree',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5b66\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='eduction',
            name='major',
            field=models.CharField(max_length=50, null=True, verbose_name='\u4e13\u4e1a', blank=True),
        ),
        migrations.AlterField(
            model_name='historicaleduction',
            name='degree',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5b66\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='historicaleduction',
            name='major',
            field=models.CharField(max_length=50, null=True, verbose_name='\u4e13\u4e1a', blank=True),
        ),
    ]
