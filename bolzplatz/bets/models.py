from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100, blank=True)
    team = models.ForeignKey(Team,
                             related_name='player_team',
                             on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.team)


class Match(models.Model):
    team_home = models.ForeignKey(Team, related_name='match_team_home')
    team_visitor = models.ForeignKey(Team, related_name='match_team_visitor')
    score_home = models.PositiveIntegerField(null=True, blank=True, default=None)
    score_visitor = models.PositiveIntegerField(null=True, blank=True, default=None)
    location = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField()
    overtime = models.BooleanField(default=False)
    penalty = models.BooleanField(default=False)

    def __str__(self):
        return '{} : {} ({})'.format(
            self.team_home,
            self.team_visitor,
            self.date.strftime('%B %d'))


class Bet(models.Model):
    match = models.ForeignKey(Match, verbose_name='Spiel')
    profile = models.ForeignKey('users.Profile')
    score_home = models.PositiveIntegerField()
    score_visitor = models.PositiveIntegerField()
    checked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}] {}'.format(
            self.profile,
            self.match)
