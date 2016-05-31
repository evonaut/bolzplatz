from django.conf.urls import include, url
from django.contrib import admin

from users import urls as users_urls
from bets import urls as bets_urls
from scores import urls as scores_urls

admin.site.site_header = 'Bolzplatz Admin'
admin.site.site_title = 'Bolzplatz Site Admin'

urlpatterns = [
    url(r'^', include(bets_urls), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include(users_urls, app_name='users', namespace='auth'),),
    url(r'^bets/', include(bets_urls, app_name='bets', namespace='bets'),),
    url(r'^scores/', include(scores_urls, app_name='scores', namespace='scores'),),
]
