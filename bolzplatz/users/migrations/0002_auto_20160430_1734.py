# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('slug', models.SlugField(unique=True, max_length=30)),
                ('about', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(default='', to='users.Group'),
            preserve_default=False,
        ),
    ]
