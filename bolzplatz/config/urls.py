from django.conf.urls import include, url
from django.contrib import admin

from users import urls as users_urls

admin.site.site_header = ' Bolzplatz Admin'
admin.site.site_title = 'Bolzplatz Site Admin'

urlpatterns = [
    # Examples:
    # url(r'^$', 'bolzplatz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/',
        include(users_urls, app_name='users', namespace='auth'),
        ),
    url(r'^bets/', include('bets.urls')),
]
