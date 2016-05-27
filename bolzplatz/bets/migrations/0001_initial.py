# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160430_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('score_home', models.IntegerField()),
                ('score_visitor', models.IntegerField()),
                ('checked', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('score_home', models.IntegerField(blank=True)),
                ('score_visitor', models.IntegerField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('overtime', models.BooleanField(default=False)),
                ('penalty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.TextField()),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.TextField()),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name='player_team', to='bets.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_home',
            field=models.ForeignKey(related_name='match_team_home', to='bets.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_visitor',
            field=models.ForeignKey(related_name='match_team_visitor', to='bets.Team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(to='bets.Match'),
        ),
        migrations.AddField(
            model_name='bet',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
        ),
    ]
