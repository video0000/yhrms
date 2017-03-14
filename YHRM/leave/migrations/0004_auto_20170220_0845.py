# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20170206_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchanging_Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u4e32\u4f11\u4e0a\u73ed\u65e5\u671f')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '\u4e32\u4f11\u4e0a\u73ed\u4fe1\u606f',
                'verbose_name_plural': '\u4e32\u4f11\u4e0a\u73ed\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='\u8282\u65e5\u540d\u79f0')),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name': '\u8282\u65e5\u4fe1\u606f',
                'verbose_name_plural': '\u8282\u65e5\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='exchanging_holiday',
            name='holiday',
            field=models.ForeignKey(related_name='exchanging_holiday', verbose_name='\u8282\u65e5\u4fe1\u606f', to='leave.Holiday'),
        ),
    ]
