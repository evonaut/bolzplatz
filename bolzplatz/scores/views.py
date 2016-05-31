from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator

from users.models import Profile, Group


class ScoreHome(View):
    template_name = 'scores/scores_home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        profiles = []
        if slug is not None:
            try:
                profiles = Profile.objects.filter(group=Group.objects.get(slug=slug)).order_by('score').reverse()
                group = slug
            except:
                pass
        if not profiles:
            profiles = Profile.objects.all().order_by('score').reverse()
            group = 'All Groups'

        return render(
            request,
            self.template_name,
            {'profiles': profiles,
             'group': group}
        )
