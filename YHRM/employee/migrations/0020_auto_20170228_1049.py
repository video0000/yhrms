# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_dimission_historicaldimission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_joined_bccb',
            field=models.DateField(null=True, verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_start_working',
            field=models.DateField(null=True, verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='date_of_joined_bccb',
            field=models.DateField(null=True, verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='date_of_start_working',
            field=models.DateField(null=True, verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4', blank=True),
        ),
    ]
