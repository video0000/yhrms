# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20170116_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eduction',
            options={'ordering': ['employee', '-start_date'], 'verbose_name': '\u5b66\u5386\u4fe1\u606f', 'verbose_name_plural': '\u5b66\u5386\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='transferorder',
            options={'ordering': ['employee', '-transfer_date'], 'verbose_name': '\u8c03\u4ee4', 'verbose_name_plural': '\u8c03\u4ee4'},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['employee', '-start_date'], 'verbose_name': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386', 'verbose_name_plural': '\u672c\u5355\u4f4d\u5de5\u4f5c\u7ecf\u5386'},
        ),
    ]
