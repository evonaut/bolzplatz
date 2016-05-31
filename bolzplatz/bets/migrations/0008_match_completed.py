# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0007_auto_20160531_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
