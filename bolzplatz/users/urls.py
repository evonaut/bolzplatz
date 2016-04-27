from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'users/login.html'},
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'users/logout.html',
         'extra_context':
             {'form': AuthenticationForm}},
        name='logout'),
]
