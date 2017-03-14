# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0018_auto_20170116_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dimission_date', models.DateField(verbose_name='\u79bb\u804c\u65e5\u671f')),
                ('record_date', models.DateField(auto_now_add=True, verbose_name='\u767b\u8bb0\u65e5\u671f')),
                ('reason', models.TextField(verbose_name='\u79bb\u804c\u539f\u56e0')),
                ('employee', models.OneToOneField(related_name='dimissions', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
            ],
            options={
                'ordering': ['-record_date'],
                'verbose_name': '\u79bb\u804c',
                'verbose_name_plural': '\u79bb\u804c',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDimission',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('dimission_date', models.DateField(verbose_name='\u79bb\u804c\u65e5\u671f')),
                ('record_date', models.DateField(verbose_name='\u767b\u8bb0\u65e5\u671f', editable=False, blank=True)),
                ('reason', models.TextField(verbose_name='\u79bb\u804c\u539f\u56e0')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u79bb\u804c',
            },
        ),
    ]
