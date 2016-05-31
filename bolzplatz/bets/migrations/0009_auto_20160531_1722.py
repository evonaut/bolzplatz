# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0008_match_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='checked',
        ),
        migrations.AddField(
            model_name='bet',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
