# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0004_auto_20160529_0836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterUniqueTogether(
            name='bet',
            unique_together=set([('match', 'user')]),
        ),
    ]
