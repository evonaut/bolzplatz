from django.contrib import admin

from .models import Team, Match, Bet


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):

    def bet_count(self, obj):
        return obj.bet_set.count()

    def match_name(self, obj):
        return '{} : {}'.format(obj.team_home, obj.team_visitor)

    bet_count.short_description = "Bet Count"
    match_name.short_description = "Match"

    list_display = ('date', 'match_name', 'completed', 'bet_count')
    list_filter = ('date', 'completed', 'team_home', 'team_visitor',)
    date_hierarchy = 'date'
    search_fields = ('team_home__name', 'team_visitor__name')
    ordering = ('date',)


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):

    def bet_display(self, obj):
        return '{} : {}'.format(obj.score_home, obj.score_visitor)

    bet_display.short_description = "Bet"

    list_display = ('match', 'user', 'modified', 'bet_display', 'score')
    list_filter = ('match',)
    date_hierarchy = 'modified'
    search_fields = ('user__username',)
    ordering = ('user', 'modified')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def match_count(self, obj):
        home_count = obj.match_team_home.count()
        visitor_count = obj.match_team_visitor.count()
        return home_count + visitor_count

    match_count.short_description = "Match Count"

    list_display = ('name', 'match_count')
    ordering = ('name',)
