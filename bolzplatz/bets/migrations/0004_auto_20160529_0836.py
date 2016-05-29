# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bets', '0003_auto_20160527_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='profile',
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(default=1, related_name='bets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(verbose_name='Spiel', to='bets.Match'),
        ),
    ]
