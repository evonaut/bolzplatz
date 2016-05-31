from django.conf.urls import include, url, patterns

from .views import ScoreHome

urlpatterns = patterns('',
                       url(r'^$', ScoreHome.as_view(), name='scores_home'),
                       url(r'^(?P<slug>\w.*)$', ScoreHome.as_view(), name='scores_home'),
                       )
