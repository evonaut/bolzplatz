# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
