# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_number', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('type', models.CharField(default=b'', choices=[(b'zh', '\u603b\u884c'), (b'zhbm', '\u603b\u884c\u90e8\u95e8'), (b'yjzh', '\u4e00\u7ea7\u884c'), (b'ejzh', '\u4e8c\u7ea7\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('address', models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('parent_structure', models.ForeignKey(related_name='children', blank=True, to='department.Department', max_length=50, null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe6\x9c\xba\xe6\x9e\x84')),
            ],
            options={
                'ordering': ['department_number'],
                'verbose_name': '\u673a\u6784\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u6784\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDepartment',
            fields=[
                ('department_number', models.CharField(max_length=20, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xbc\x96\xe5\x8f\xb7', db_index=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('type', models.CharField(default=b'', choices=[(b'zh', '\u603b\u884c'), (b'zhbm', '\u603b\u884c\u90e8\u95e8'), (b'yjzh', '\u4e00\u7ea7\u884c'), (b'ejzh', '\u4e8c\u7ea7\u652f\u884c')], max_length=20, blank=True, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('address', models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent_structure', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u673a\u6784\u4fe1\u606f',
            },
        ),
    ]
