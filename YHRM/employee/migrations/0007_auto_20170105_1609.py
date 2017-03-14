# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20170104_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['-start_date'], 'verbose_name': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386', 'verbose_name_plural': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386'},
        ),
        migrations.AlterField(
            model_name='historicalworkexperience',
            name='end_date',
            field=models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f', blank=True),
        ),
    ]
