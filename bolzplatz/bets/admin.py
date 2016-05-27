from django.contrib import admin

from .models import Player, Team, Match, Bet

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Bet)