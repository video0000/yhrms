# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20170103_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='duration',
            field=models.CharField(default=b'long_term', max_length=50, verbose_name='\u5408\u540c\u671f\u9650', choices=[('\u4e09\u5e74', '\u4e09\u5e74'), ('\u957f\u671f', '\u957f\u671f')]),
        ),
        migrations.AlterField(
            model_name='eduction',
            name='qualification',
            field=models.CharField(default=b'Undergraduate', max_length=50, verbose_name='\u5b66\u5386', choices=[('\u5c0f\u5b66', '\u5c0f\u5b66'), ('\u521d\u4e2d', '\u521d\u4e2d'), ('\u9ad8\u4e2d', '\u9ad8\u4e2d'), ('\u4e2d\u4e13', '\u4e2d\u4e13'), ('\u5927\u4e13', '\u5927\u4e13'), ('\u672c\u79d1', '\u672c\u79d1'), ('\u7814\u7a76\u751f', '\u7814\u7a76\u751f'), ('\u535a\u58eb', '\u535a\u58eb')]),
        ),
        migrations.AlterField(
            model_name='eduction',
            name='type',
            field=models.CharField(max_length=50, verbose_name='\u5b66\u5386\u7c7b\u578b', choices=[('\u7b2c\u4e00\u5b66\u5386', '\u7b2c\u4e00\u5b66\u5386'), ('\u73b0\u5b66\u5386', '\u73b0\u5b66\u5386'), ('\u5176\u4ed6\u7c7b\u578b\u5b66\u5386', '\u5176\u4ed6\u7c7b\u578b\u5b66\u5386')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[('\u9886\u5bfc\u73ed\u5b50', '\u9886\u5bfc\u73ed\u5b50'), ('\u4e2d\u5c42\u6b63\u804c', '\u4e2d\u5c42\u6b63\u804c'), ('\u4e2d\u5c42\u526f\u804c', '\u4e2d\u5c42\u526f\u804c'), ('\u6b63\u5f0f\u5728\u5c97\u5458\u5de5', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), ('\u4ee3\u529e\u5458', '\u4ee3\u529e\u5458'), ('\u79bb\u5c97\u4f11\u517b\u5e72\u90e8', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), ('\u79bb\u5c97\u4f11\u517b\u5458\u5de5', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), ('\u5185\u9000', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=b'male', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='political_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[('\u515a\u5458', '\u515a\u5458'), ('\u7fa4\u4f17', '\u7fa4\u4f17'), ('\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')]),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='duration',
            field=models.CharField(default=b'long_term', max_length=50, verbose_name='\u5408\u540c\u671f\u9650', choices=[('\u4e09\u5e74', '\u4e09\u5e74'), ('\u957f\u671f', '\u957f\u671f')]),
        ),
        migrations.AlterField(
            model_name='historicaleduction',
            name='qualification',
            field=models.CharField(default=b'Undergraduate', max_length=50, verbose_name='\u5b66\u5386', choices=[('\u5c0f\u5b66', '\u5c0f\u5b66'), ('\u521d\u4e2d', '\u521d\u4e2d'), ('\u9ad8\u4e2d', '\u9ad8\u4e2d'), ('\u4e2d\u4e13', '\u4e2d\u4e13'), ('\u5927\u4e13', '\u5927\u4e13'), ('\u672c\u79d1', '\u672c\u79d1'), ('\u7814\u7a76\u751f', '\u7814\u7a76\u751f'), ('\u535a\u58eb', '\u535a\u58eb')]),
        ),
        migrations.AlterField(
            model_name='historicaleduction',
            name='type',
            field=models.CharField(max_length=50, verbose_name='\u5b66\u5386\u7c7b\u578b', choices=[('\u7b2c\u4e00\u5b66\u5386', '\u7b2c\u4e00\u5b66\u5386'), ('\u73b0\u5b66\u5386', '\u73b0\u5b66\u5386'), ('\u5176\u4ed6\u7c7b\u578b\u5b66\u5386', '\u5176\u4ed6\u7c7b\u578b\u5b66\u5386')]),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[('\u9886\u5bfc\u73ed\u5b50', '\u9886\u5bfc\u73ed\u5b50'), ('\u4e2d\u5c42\u6b63\u804c', '\u4e2d\u5c42\u6b63\u804c'), ('\u4e2d\u5c42\u526f\u804c', '\u4e2d\u5c42\u526f\u804c'), ('\u6b63\u5f0f\u5728\u5c97\u5458\u5de5', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), ('\u4ee3\u529e\u5458', '\u4ee3\u529e\u5458'), ('\u79bb\u5c97\u4f11\u517b\u5e72\u90e8', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), ('\u79bb\u5c97\u4f11\u517b\u5458\u5de5', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), ('\u5185\u9000', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='gender',
            field=models.CharField(default=b'male', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=20, blank=True, null=True, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='political_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', choices=[('\u515a\u5458', '\u515a\u5458'), ('\u7fa4\u4f17', '\u7fa4\u4f17'), ('\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e', '\u5176\u4ed6\u6c11\u4e3b\u515a\u6d3e')]),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='department',
            field=models.ForeignKey(verbose_name='\u90e8\u95e8', to='department.Department'),
        ),
    ]
