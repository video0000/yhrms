# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalleave',
            options={'ordering': ('-history_date', '-history_id'), 'get_latest_by': 'history_date', 'verbose_name': 'historical \u4f11\u5047\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='leave',
            options={'ordering': ['employee', '-start_date'], 'verbose_name': '\u4f11\u5047\u4fe1\u606f', 'verbose_name_plural': '\u4f11\u5047\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='leave',
            name='employee',
            field=models.ForeignKey(related_name='leaves', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee'),
        ),
    ]
