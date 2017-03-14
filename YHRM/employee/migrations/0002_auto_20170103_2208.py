# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='duration',
            field=models.CharField(default='long_term', max_length=50, verbose_name='\u5408\u540c\u671f\u9650', choices=[(b'three_years', '\u4e09\u5e74'), (b'long_term', '\u957f\u671f')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalcontract',
            name='duration',
            field=models.CharField(default=2, max_length=50, verbose_name='\u5408\u540c\u671f\u9650', choices=[(b'three_years', '\u4e09\u5e74'), (b'long_term', '\u957f\u671f')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='eduction',
            name='qualification',
            field=models.CharField(default=b'Undergraduate', max_length=50, verbose_name='\u5b66\u5386', choices=[(b'Primary School', '\u5c0f\u5b66'), (b'Junior middle School', '\u521d\u4e2d'), (b'high school', '\u9ad8\u4e2d'), (b'Secondary specialized school', '\u4e2d\u4e13'), (b'Junior College', '\u5927\u4e13'), (b'Undergraduate', '\u672c\u79d1'), (b'Graduate student', '\u7814\u7a76\u751f'), (b'doctorate', '\u535a\u58eb')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.DateField(verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_joined_bccb',
            field=models.DateField(verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_start_working',
            field=models.DateField(verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[(b'leadership', '\u9886\u5bfc\u73ed\u5b50'), (b'Middle Administrator', '\u4e2d\u5c42\u6b63\u804c'), (b'Middle Vicd-Adminstrator', '\u4e2d\u5c42\u526f\u804c'), (b'Formal Staff', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), (b'Agent', '\u4ee3\u529e\u5458'), (b'Leaved Cadre', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), (b'Leaved Staff', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), (b'Early Retirement', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
        migrations.AlterField(
            model_name='historicalcontract',
            name='start_date',
            field=models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='historicaleduction',
            name='qualification',
            field=models.CharField(default=b'Undergraduate', max_length=50, verbose_name='\u5b66\u5386', choices=[(b'Primary School', '\u5c0f\u5b66'), (b'Junior middle School', '\u521d\u4e2d'), (b'high school', '\u9ad8\u4e2d'), (b'Secondary specialized school', '\u4e2d\u4e13'), (b'Junior College', '\u5927\u4e13'), (b'Undergraduate', '\u672c\u79d1'), (b'Graduate student', '\u7814\u7a76\u751f'), (b'doctorate', '\u535a\u58eb')]),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='birthday',
            field=models.DateField(verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='date_of_joined_bccb',
            field=models.DateField(verbose_name='\u5230\u5546\u5de5\u4f5c\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='date_of_start_working',
            field=models.DateField(verbose_name='\u53c2\u52a0\u5de5\u4f5c\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='employee_type',
            field=models.CharField(default=b'Formal Staff', choices=[(b'leadership', '\u9886\u5bfc\u73ed\u5b50'), (b'Middle Administrator', '\u4e2d\u5c42\u6b63\u804c'), (b'Middle Vicd-Adminstrator', '\u4e2d\u5c42\u526f\u804c'), (b'Formal Staff', '\u6b63\u5f0f\u5728\u5c97\u5458\u5de5'), (b'Agent', '\u4ee3\u529e\u5458'), (b'Leaved Cadre', '\u79bb\u5c97\u4f11\u517b\u5e72\u90e8'), (b'Leaved Staff', '\u79bb\u5c97\u4f11\u517b\u5458\u5de5'), (b'Early Retirement', '\u5185\u9000')], max_length=20, blank=True, null=True, verbose_name='\u5458\u5de5\u6027\u8d28'),
        ),
    ]
