from django.conf.urls import include, url, patterns

from .views import BetHome, BetCreate, BetChange, BetEvaluate, bet_stats, bet_rules, bet_imprint

urlpatterns = patterns('',
                       url(r'^$', BetHome.as_view(), name='bets_home'),
                       url(r'^create/$', BetCreate.as_view(), name='bets_create'),
                       url(r'^change/(?P<id>\d+)$', BetChange.as_view(), name='bets_change'),
                       url(r'^eval/$', BetEvaluate.as_view(), name='bets_evaluate'),
                       url(r'^stats/$', bet_stats, name='bets_stats'),
                       url(r'^rules/$', bet_rules, name='bets_rules'),
                       url(r'^imprint/$', bet_imprint, name='bets_imprint')
                       )
