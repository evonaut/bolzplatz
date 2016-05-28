from django.conf.urls import include, url, patterns

from .views import BetCreate

urlpatterns = patterns('',
                       url(r'^$',
                           'bets.views.home',
                           name='bets_home'),
                       url(r'^create/$',
                           BetCreate.as_view(),
                           name='bets_create')
                       )
