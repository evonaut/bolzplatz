from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView, TemplateView

from .views import CreateAccount

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            pattern_name='auth:login',
            permanent=False)),
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
    url(r'^create/$',
        CreateAccount.as_view(),
        name='create'),
    url(r'^create/done/$',
        TemplateView.as_view(
            template_name=(
                'users/user_create_done.html')),
        name='create_done'),
]
