# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20170103_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='pdf',
            field=models.FileField(upload_to=b'employee/contract', null=True, verbose_name='\u5408\u540c\u5f71\u5370', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(related_name='employees', verbose_name='\u90e8\u95e8', blank=True, to='department.Department', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[(b'leadership', '\u9886\u5bfc\u73ed\u5b50'), (b'Middle Administrator', '\u4e2d\u5c42\u6b63\u804c'), (b'Middle Vicd-Adminstrator', '\u4e2d\u5c42\u526f\u804c'), (b'Formal Staff', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), (b'Agent', '\u4ee3\u529e\u5458'), (b'Leaved Cadre', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), (b'Leaved Staff', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), (b'Early Retirement', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=b'male', choices=[(b'male', '\u7537'), (b'female', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='home_address',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5bb6\u5ead\u4f4f\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='identification_card',
            field=models.CharField(max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5458\u5de5\u59d3\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationality',
            field=models.CharField(default='\u6c49\u65cf', max_length=10, null=True, verbose_name='\u6c11\u65cf', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='political_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[(b'party', '\u515a\u5458'), (b'No_spported_political_party', '\u7fa4\u4f17'), (b'other_spported_political_party', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='titles',
            field=models.CharField(max_length=50, null=True, verbose_name='\u804c\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='pdf',
            field=models.TextField(max_length=100, null=True, verbose_name='\u5408\u540c\u5f71\u5370', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[(b'leadership', '\u9886\u5bfc\u73ed\u5b50'), (b'Middle Administrator', '\u4e2d\u5c42\u6b63\u804c'), (b'Middle Vicd-Adminstrator', '\u4e2d\u5c42\u526f\u804c'), (b'Formal Staff', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), (b'Agent', '\u4ee3\u529e\u5458'), (b'Leaved Cadre', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), (b'Leaved Staff', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), (b'Early Retirement', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='gender',
            field=models.CharField(default=b'male', choices=[(b'male', '\u7537'), (b'female', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='home_address',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5bb6\u5ead\u4f4f\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='identification_card',
            field=models.CharField(max_length=20, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5458\u5de5\u59d3\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='nationality',
            field=models.CharField(default='\u6c49\u65cf', max_length=10, null=True, verbose_name='\u6c11\u65cf', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='political_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[(b'party', '\u515a\u5458'), (b'No_spported_political_party', '\u7fa4\u4f17'), (b'other_spported_political_party', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')]),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='titles',
            field=models.CharField(max_length=50, null=True, verbose_name='\u804c\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalrelationship',
            name='graduate_from',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalrelationship',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u804c\u52a1\u6216\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalrelationship',
            name='political_status',
            field=models.CharField(max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalworkexperience',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='graduate_from',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u804c\u52a1\u6216\u5c97\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='political_status',
            field=models.CharField(max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', blank=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5c97\u4f4d', blank=True),
        ),
    ]
