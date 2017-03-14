# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_auto_20170111_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransferorder',
            name='new_department',
            field=models.CharField(max_length=50, null=True, verbose_name='\u73b0\u90e8\u95e8', blank=True),
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='new_department',
            field=models.CharField(max_length=50, null=True, verbose_name='\u73b0\u90e8\u95e8', blank=True),
        ),
    ]
