# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20170111_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='employee',
            field=models.ForeignKey(related_name='contracts', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee'),
        ),
    ]
