# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_auto_20160527_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='score_home',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bet',
            name='score_visitor',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_home',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='score_visitor',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
