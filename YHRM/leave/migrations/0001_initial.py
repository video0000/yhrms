# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0019_dimission_historicaldimission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLeave',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('leave_type', models.CharField(default='\u5e74\u5047', max_length=20, verbose_name='\u4f11\u5047\u7c7b\u578b', choices=[('\u5e74\u5047', '\u5e74\u5047'), ('\u4e8b\u5047', '\u4e8b\u5047'), ('\u75c5\u5047', '\u75c5\u5047')])),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('reason', models.TextField(verbose_name='\u4f11\u5047\u539f\u56e0')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical leave',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leave_type', models.CharField(default='\u5e74\u5047', max_length=20, verbose_name='\u4f11\u5047\u7c7b\u578b', choices=[('\u5e74\u5047', '\u5e74\u5047'), ('\u4e8b\u5047', '\u4e8b\u5047'), ('\u75c5\u5047', '\u75c5\u5047')])),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('reason', models.TextField(verbose_name='\u4f11\u5047\u539f\u56e0')),
                ('employee', models.ForeignKey(verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
            ],
        ),
    ]
