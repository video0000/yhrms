# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='type',
            field=models.CharField(default=b'', choices=[(b'headquarters', '\u603b\u884c'), (b'subbranch', '\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='historicaldepartment',
            name='type',
            field=models.CharField(default=b'', choices=[(b'headquarters', '\u603b\u884c'), (b'subbranch', '\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
