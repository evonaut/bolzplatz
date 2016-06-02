from django.conf.urls import include, url, patterns

from .views import BetHome, BetCreate, BetEvaluate, bet_rules

urlpatterns = patterns('',
                       url(r'^$', BetHome.as_view(), name='bets_home'),
                       url(r'^create/$', BetCreate.as_view(), name='bets_create'),
                       url(r'^eval/$', BetEvaluate.as_view(), name='bets_evaluate'),
                       url(r'^rules/$', bet_rules, name='bets_rules')
                       )
