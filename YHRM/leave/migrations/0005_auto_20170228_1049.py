# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_auto_20170220_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalleave',
            name='leave_type',
            field=models.CharField(default='\u5e74\u5047', max_length=20, verbose_name='\u4f11\u5047\u7c7b\u578b', choices=[('\u5e74\u5047', '\u5e74\u5047'), ('\u4e8b\u5047', '\u4e8b\u5047'), ('\u75c5\u5047', '\u75c5\u5047'), ('\u5a5a\u5047', '\u5a5a\u5047'), ('\u4ea7\u5047\u53ca\u62a4\u7406\u5047', '\u4ea7\u5047\u53ca\u62a4\u7406\u5047'), ('\u54fa\u4e73\u5047', '\u54fa\u4e73\u5047'), ('\u4e27\u5047', '\u4e27\u5047'), ('\u63a2\u4eb2\u5047', '\u63a2\u4eb2\u5047')]),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(default='\u5e74\u5047', max_length=20, verbose_name='\u4f11\u5047\u7c7b\u578b', choices=[('\u5e74\u5047', '\u5e74\u5047'), ('\u4e8b\u5047', '\u4e8b\u5047'), ('\u75c5\u5047', '\u75c5\u5047'), ('\u5a5a\u5047', '\u5a5a\u5047'), ('\u4ea7\u5047\u53ca\u62a4\u7406\u5047', '\u4ea7\u5047\u53ca\u62a4\u7406\u5047'), ('\u54fa\u4e73\u5047', '\u54fa\u4e73\u5047'), ('\u4e27\u5047', '\u4e27\u5047'), ('\u63a2\u4eb2\u5047', '\u63a2\u4eb2\u5047')]),
        ),
    ]
