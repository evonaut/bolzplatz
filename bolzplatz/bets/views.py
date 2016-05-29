from django.shortcuts import get_object_or_404, redirect, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import View

from .forms import BetForm
from .utils import BetFormValidMixin


def home(request):
    """
    Default view
    """
    return render(request, 'bets/bets_home.html')


class BetCreate(BetFormValidMixin, View):
    form_class = BetForm
    template_name = 'bets/bets_create.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()}
        )

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_bet = bound_form.save(request)
            return redirect('bets:bets_create')
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form}
            )