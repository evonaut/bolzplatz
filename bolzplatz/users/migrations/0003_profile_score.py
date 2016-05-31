# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160430_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
