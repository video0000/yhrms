# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20170103_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='type',
            field=models.CharField(default=b'', choices=[('\u603b\u884c', '\u603b\u884c'), ('\u603b\u884c\u73ed\u5b50', '\u603b\u884c\u73ed\u5b50'), ('\u603b\u884c\u4e1a\u52a1\u90e8\u5ba4', '\u603b\u884c\u4e1a\u52a1\u90e8\u5ba4'), ('\u603b\u884c\u5176\u4ed6\u90e8\u5ba4', '\u603b\u884c\u5176\u4ed6\u90e8\u5ba4'), ('\u652f\u884c', '\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='historicaldepartment',
            name='type',
            field=models.CharField(default=b'', choices=[('\u603b\u884c', '\u603b\u884c'), ('\u603b\u884c\u73ed\u5b50', '\u603b\u884c\u73ed\u5b50'), ('\u603b\u884c\u4e1a\u52a1\u90e8\u5ba4', '\u603b\u884c\u4e1a\u52a1\u90e8\u5ba4'), ('\u603b\u884c\u5176\u4ed6\u90e8\u5ba4', '\u603b\u884c\u5176\u4ed6\u90e8\u5ba4'), ('\u652f\u884c', '\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
