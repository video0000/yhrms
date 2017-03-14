# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_auto_20170111_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransferorder',
            name='new_department',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u73b0\u90e8\u95e8', choices=[('bccb', '\u672c\u6eaa\u5e02\u5546\u4e1a\u94f6\u884c'), ('bwb', '\u4fdd\u536b\u90e8'), ('jhc', '\u7a3d\u6838\u5904'), ('rsc', '\u4eba\u4e8b\u5904')]),
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='new_department',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u73b0\u90e8\u95e8', choices=[('bccb', '\u672c\u6eaa\u5e02\u5546\u4e1a\u94f6\u884c'), ('bwb', '\u4fdd\u536b\u90e8'), ('jhc', '\u7a3d\u6838\u5904'), ('rsc', '\u4eba\u4e8b\u5904')]),
        ),
    ]
