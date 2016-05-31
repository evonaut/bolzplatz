# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0005_auto_20160529_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bet',
            options={'permissions': ('evaluate_bets', 'Can evaluate bets')},
        ),
    ]
