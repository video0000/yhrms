# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_auto_20170104_0956'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0007_auto_20170105_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTransferOrder',
            fields=[
                ('transfer_number', models.CharField(max_length=20, verbose_name='\u8c03\u4ee4\u53f7', db_index=True)),
                ('old_job', models.CharField(default=b'employee.job', max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True)),
                ('new_job', models.CharField(max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True)),
                ('transfer_date', models.DateField(verbose_name='\u8c03\u52a8\u65e5\u671f')),
                ('new_department_salary_calculate_start_date', models.DateField(verbose_name='\u65b0\u5355\u4f4d\u8d77\u85aa\u65e5\u671f')),
                ('transfer_reason', models.TextField(null=True, verbose_name='\u8c03\u52a8\u539f\u56e0', blank=True)),
                ('confirm', models.BooleanField(default=False, verbose_name='\u540c\u6b65\u5230\u5458\u5de5\u4fe1\u606f')),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('employee', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='employee.Employee', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('new_department', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True)),
                ('old_department', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical \u8c03\u4ee4',
            },
        ),
        migrations.CreateModel(
            name='TransferOrder',
            fields=[
                ('transfer_number', models.CharField(max_length=20, serialize=False, verbose_name='\u8c03\u4ee4\u53f7', primary_key=True)),
                ('old_job', models.CharField(default=b'employee.job', max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True)),
                ('new_job', models.CharField(max_length=50, null=True, verbose_name='\u73b0\u5c97\u4f4d', blank=True)),
                ('transfer_date', models.DateField(verbose_name='\u8c03\u52a8\u65e5\u671f')),
                ('new_department_salary_calculate_start_date', models.DateField(verbose_name='\u65b0\u5355\u4f4d\u8d77\u85aa\u65e5\u671f')),
                ('transfer_reason', models.TextField(null=True, verbose_name='\u8c03\u52a8\u539f\u56e0', blank=True)),
                ('confirm', models.BooleanField(default=False, verbose_name='\u540c\u6b65\u5230\u5458\u5de5\u4fe1\u606f')),
                ('employee', models.ForeignKey(related_name='transferorders_by_employee', verbose_name='\u5458\u5de5\u7f16\u53f7', to='employee.Employee')),
                ('new_department', models.ForeignKey(related_name='transferorders_by_department', verbose_name='\u73b0\u90e8\u95e8', blank=True, to='department.Department', null=True)),
                ('old_department', models.ForeignKey(related_name='transferorders_by_department_old', default=b'employee.department.department_number', blank=True, to='department.Department', null=True, verbose_name='\u73b0\u90e8\u95e8')),
            ],
            options={
                'verbose_name': '\u8c03\u4ee4',
                'verbose_name_plural': '\u8c03\u4ee4',
            },
        ),
        migrations.AlterField(
            model_name='historicalrelationship',
            name='graduate_from',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821\u53ca\u4e13\u4e1a', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalrelationship',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5de5\u4f5c\u5355\u4f4d\u53ca\u804c\u52a1', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='graduate_from',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821\u53ca\u4e13\u4e1a', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5de5\u4f5c\u5355\u4f4d\u53ca\u804c\u52a1', blank=True),
        ),
    ]
