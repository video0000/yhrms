# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_auto_20170111_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltransferorder',
            name='new_department',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True),
        ),
        migrations.AlterField(
            model_name='historicaltransferorder',
            name='old_department',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='department.Department', null=True),
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='new_department',
            field=models.ForeignKey(related_name='transfer_order_by_new_department', default='', verbose_name='\u73b0\u90e8\u95e8', to='department.Department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transferorder',
            name='old_department',
            field=models.ForeignKey(related_name='transfer_order_by_old_department', default='', verbose_name='\u539f\u90e8\u95e8', to='department.Department'),
            preserve_default=False,
        ),
    ]
