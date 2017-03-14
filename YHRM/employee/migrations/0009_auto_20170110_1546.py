# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20170110_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransferorder',
            name='old_job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='old_department',
            field=models.ForeignKey(related_name='transferorders_by_department_old', verbose_name='\u73b0\u90e8\u95e8', blank=True, to='department.Department', null=True),
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='old_job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True),
        ),
    ]
