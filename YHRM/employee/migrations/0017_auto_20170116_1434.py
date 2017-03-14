# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_auto_20170116_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['employee', '-start_date'], 'verbose_name': '\u5408\u540c\u4fe1\u606f', 'verbose_name_plural': '\u5408\u540c\u4fe1\u606f'},
        ),
    ]
