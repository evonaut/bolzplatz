from django.shortcuts import get_object_or_404, redirect, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import BetForm
from .utils import BetFormValidMixin
from .models import Bet, Match


@login_required
def home(request):
    """
    Default view
    """
    return render(request, 'bets/bets_home.html')


class BetCreate(BetFormValidMixin, View):
    form_class = BetForm
    template_name = 'bets/bets_create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        form.fields['match'].queryset = Match.objects.exclude(bet__user=request.user)
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request):
        bound_form = self.form_class(request.POST, user=request.user)
        if bound_form.is_valid():
            new_bet = bound_form.save(request)
            return redirect('bets:bets_create')
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form}
            )
