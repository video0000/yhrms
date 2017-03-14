# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20170103_1628'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, verbose_name='\u5f00\u59cb\u65e5\u671f', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f', blank=True)),
                ('pdf', models.FileField(upload_to=b'employee/contract', null=True, verbose_name='\u5408\u540c\u5f71\u5370', blank=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c\u4fe1\u606f',
                'verbose_name_plural': '\u5408\u540c\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Eduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('qualification', models.CharField(max_length=50, verbose_name='\u5b66\u5386')),
                ('degree', models.CharField(max_length=50, verbose_name='\u5b66\u4f4d')),
                ('major', models.CharField(max_length=50, verbose_name='\u4e13\u4e1a')),
                ('graduate_from', models.CharField(max_length=200, verbose_name='\u6bd5\u4e1a\u9662\u6821')),
                ('type', models.CharField(max_length=50, verbose_name='\u5b66\u5386\u7c7b\u578b', choices=[(b'first', '\u7b2c\u4e00\u5b66\u5386'), (b'now', '\u73b0\u5b66\u5386'), (b'others', '\u5176\u4ed6\u7c7b\u578b\u5b66\u5386')])),
            ],
            options={
                'verbose_name': '\u5b66\u5386\u4fe1\u606f',
                'verbose_name_plural': '\u5b66\u5386\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_number', models.CharField(max_length=20, serialize=False, verbose_name='\u5458\u5de5\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='\u5458\u5de5\u59d3\u540d', blank=True)),
                ('atatar', models.ImageField(default=b'employee/avatar/default.jpg', upload_to=b'employee/avatar/', null=True, verbose_name='\u7167\u7247', blank=True)),
                ('gender', models.CharField(default=b'male', choices=[(b'male', '\u7537'), (b'female', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b')),
                ('nationality', models.CharField(default='\u6c49\u65cf', max_length=10, null=True, verbose_name='\u6c11\u65cf', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('date_of_start_working', models.DateField(null=True, verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('date_of_joined_bccb', models.DateField(null=True, verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('employee_type', models.CharField(max_length=20, null=True, verbose_name='\u5458\u5de5\u6027\u8d28', blank=True)),
                ('titles', models.CharField(max_length=50, null=True, verbose_name='\u804c\u79f0', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True)),
                ('political_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[(b'party', '\u515a\u5458'), (b'No_spported_political_party', '\u7fa4\u4f17'), (b'other_spported_political_party', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')])),
                ('political_joined_date', models.DateField(null=True, verbose_name='\u5165\u515a\u65e5\u671f', blank=True)),
                ('identification_card', models.CharField(max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801', blank=True)),
                ('home_address', models.CharField(max_length=100, null=True, verbose_name='\u5bb6\u5ead\u4f4f\u5740', blank=True)),
                ('department', models.ForeignKey(related_name='employees', verbose_name='\u90e8\u95e8', blank=True, to='department.Department', null=True)),
            ],
            options={
                'ordering': ['employee_number'],
                'verbose_name': '\u5458\u5de5\u4fe1\u606f',
                'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoricalContract',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='\u5f00\u59cb\u65e5\u671f', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f', blank=True)),
                ('pdf', models.TextField(max_length=100, null=True, verbose_name='\u5408\u540c\u5f71\u5370', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u5408\u540c\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEduction',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('qualification', models.CharField(max_length=50, verbose_name='\u5b66\u5386')),
                ('degree', models.CharField(max_length=50, verbose_name='\u5b66\u4f4d')),
                ('major', models.CharField(max_length=50, verbose_name='\u4e13\u4e1a')),
                ('graduate_from', models.CharField(max_length=200, verbose_name='\u6bd5\u4e1a\u9662\u6821')),
                ('type', models.CharField(max_length=50, verbose_name='\u5b66\u5386\u7c7b\u578b', choices=[(b'first', '\u7b2c\u4e00\u5b66\u5386'), (b'now', '\u73b0\u5b66\u5386'), (b'others', '\u5176\u4ed6\u7c7b\u578b\u5b66\u5386')])),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u5b66\u5386\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('employee_number', models.CharField(max_length=20, verbose_name='\u5458\u5de5\u7f16\u53f7', db_index=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='\u5458\u5de5\u59d3\u540d', blank=True)),
                ('atatar', models.TextField(default=b'employee/avatar/default.jpg', max_length=100, null=True, verbose_name='\u7167\u7247', blank=True)),
                ('gender', models.CharField(default=b'male', choices=[(b'male', '\u7537'), (b'female', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b')),
                ('nationality', models.CharField(default='\u6c49\u65cf', max_length=10, null=True, verbose_name='\u6c11\u65cf', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('date_of_start_working', models.DateField(null=True, verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('date_of_joined_bccb', models.DateField(null=True, verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('employee_type', models.CharField(max_length=20, null=True, verbose_name='\u5458\u5de5\u6027\u8d28', blank=True)),
                ('titles', models.CharField(max_length=50, null=True, verbose_name='\u804c\u79f0', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True)),
                ('political_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[(b'party', '\u515a\u5458'), (b'No_spported_political_party', '\u7fa4\u4f17'), (b'other_spported_political_party', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')])),
                ('political_joined_date', models.DateField(null=True, verbose_name='\u5165\u515a\u65e5\u671f', blank=True)),
                ('identification_card', models.CharField(max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801', blank=True)),
                ('home_address', models.CharField(max_length=100, null=True, verbose_name='\u5bb6\u5ead\u4f4f\u5740', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('department', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u5458\u5de5\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRelationShip',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('relation', models.CharField(max_length=50, verbose_name='\u4e0e\u672c\u4eba\u5173\u7cfb')),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('political_status', models.CharField(max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', blank=True)),
                ('graduate_from', models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u804c\u52a1\u6216\u5c97\u4f4d', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u793e\u4f1a\u5173\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRemark',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('remark', models.TextField(verbose_name='\u5176\u4ed6\u9700\u8981\u8bf4\u660e\u60c5\u51b5')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u5176\u4ed6\u9700\u8981\u8bf4\u660e\u60c5\u51b5',
            },
        ),
        migrations.CreateModel(
            name='HistoricalWorkExperience',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('department', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True)),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386',
            },
        ),
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('relation', models.CharField(max_length=50, verbose_name='\u4e0e\u672c\u4eba\u5173\u7cfb')),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('political_status', models.CharField(max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', blank=True)),
                ('graduate_from', models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821', blank=True)),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u804c\u52a1\u6216\u5c97\u4f4d', blank=True)),
                ('employee', models.ForeignKey(related_name='relationships', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
            ],
            options={
                'verbose_name': '\u793e\u4f1a\u5173\u7cfb',
                'verbose_name_plural': '\u793e\u4f1a\u5173\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remark', models.TextField(verbose_name='\u5176\u4ed6\u9700\u8981\u8bf4\u660e\u60c5\u51b5')),
                ('employee', models.OneToOneField(related_name='remarks', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
            ],
            options={
                'verbose_name': '\u5176\u4ed6\u9700\u8981\u8bf4\u660e\u60c5\u51b5',
                'verbose_name_plural': '\u5176\u4ed6\u9700\u8981\u8bf4\u660e\u60c5\u51b5',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True)),
                ('department', models.ForeignKey(to='department.Department')),
                ('employee', models.ForeignKey(related_name='work_experiences', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
            ],
            options={
                'verbose_name': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386',
                'verbose_name_plural': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386',
            },
        ),
        migrations.AddField(
            model_name='eduction',
            name='employee',
            field=models.ForeignKey(related_name='eductions', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='contract',
            name='employee',
            field=models.OneToOneField(related_name='contracts', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee'),
        ),
    ]
