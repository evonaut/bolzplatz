# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='location',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='about',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='about',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
