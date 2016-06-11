from django.shortcuts import get_object_or_404, redirect, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Sum

from users.models import Profile, Group

from .forms import BetForm, BetChangeForm
from .utils import BetFormValidMixin
from .models import Bet, Match
from .decorators import require_authenticated_permission


class BetCreate(BetFormValidMixin, View):
    form_class = BetForm
    template_name = 'bets/bets_create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # Limit choices to future matches the user hasn't betted on yet
        match_query_set = Match.objects\
            .exclude(bet__user=request.user).exclude(date__lte=timezone.now())
        query_list = match_query_set[:1]
        if query_list:
            form = self.form_class(initial={'match': query_list[0]})
        else:
            form = self.form_class()
        form.fields['match'].queryset = match_query_set
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
            match_query_set = Match.objects\
                .exclude(bet__user=request.user).exclude(date__lte=timezone.now())
            query_list = match_query_set[:1]
            if query_list:
                bound_form = self.form_class(
                    request.POST,
                    user=request.user,
                    initial={'match': query_list[0]})
            else:
                bound_form = self.form_class(request.POST, user=request.user)
            bound_form.fields['match'].queryset = match_query_set
            return render(
                request,
                self.template_name,
                {'form': bound_form}
            )


class BetChange(BetFormValidMixin, View):
    form_class = BetChangeForm
    template_name = 'bets/bets_change.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_bet(self, id, user):
        try:
            bet = Bet.objects.get(pk=id)
            if bet.user != user:
                # Changing other users' bets is bad style
                bet = None
        except:
            bet = None
        return bet

    def get(self, request, id):
        bet = self.get_bet(id, request.user)
        if bet is None:
            return redirect('bets:bets_home')
        else:
            form = self.form_class(instance=bet)
            return render(
                request,
                self.template_name,
                {'id': id,
                 'bet': bet,
                 'form': form})

    def post(self, request, id):
        bet = self.get_bet(id, request.user)
        bound_form = self.form_class(
            request.POST,
            instance=bet)
        if bound_form.is_valid():
            new_bet = bound_form.save(request)
            return redirect('bets:bets_home')
        else:
            return render(
                request,
                self.template_name,
                {'id': id,
                 'bet': bet,
                 'form': bound_form})


class BetHome(View):
    template_name = 'bets/bets_home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        bets = Bet.objects.filter(user=request.user).order_by('match__date')
        now = timezone.now()
        return render(
            request,
            self.template_name,
            {'bets': bets,
             'now': now}
        )


@require_authenticated_permission('bets.evaluate_bets')
class BetEvaluate(View):
    template_name = 'bets/bets_evaluate.html'

    def _tendency(self, difference):
        if difference == 0:
            return 0
        else:
            return difference / abs(difference)

    def get(self, request):
        bets = Bet.objects.filter(score=None)
        scores = {}
        for bet in bets:
            if not bet.match.completed:
                # We don't care about matches that haven't completed yet
                continue
            if (bet.match.score_home is None) or (bet.match.score_visitor is None):
                # We can' evaluate bets on matches that have not been updated with their result
                continue
            if bet.modified > bet.match.date:
                # We don't accept bets on games that already have started
                bet.score = 0
                bet.save()
                continue
            bet_score_home = bet.score_home
            bet_score_visitor = bet.score_visitor
            score_home = bet.match.score_home
            score_visitor = bet.match.score_visitor
            diff = score_home - score_visitor
            diff_bet = bet_score_home - bet_score_visitor
            score = 0
            if self._tendency(diff_bet) == self._tendency(diff):
                # Correct tendency, that justifies two points
                score += 2
                if diff_bet == diff:
                    # Correct difference, let's add another point
                    score += 1
                    if bet_score_home == score_home:
                        # Bet is 100% correct and results in four points
                        score += 1
            user = bet.user
            try:
                user.profile.score += score
                user.profile.save()
            except ObjectDoesNotExist:
                score = 0
            bet.score = score
            bet.save()
            scores[str(user)] = scores.get(str(user), 0) + score

        return render(
            request,
            self.template_name,
            {'scores': scores}
        )


@login_required
def bet_stats(request):
    template_name = 'bets/bets_stats.html'
    stats = {
        'match_count_total': Match.objects.count(),
        'match_count_completed': Match.objects.filter(completed=True).count(),
        'bet_count_total': Bet.objects.count(),
        'bet_count_evaluated': Bet.objects.exclude(score=None).count(),
        'user_count': Profile.objects.count(),
        'group_count': Group.objects.count()
    }
    goals = Match.objects.aggregate(Sum('score_home'), Sum('score_visitor'))
    goals_total = 0
    for key in goals:
        goals_total += goals[key]
    stats['goals'] = goals_total

    return render(request,
                  template_name,
                  {'stats': stats})


@login_required
def bet_rules(request):
    return render(request, 'bets/bets_rules.html')


def bet_imprint(request):
    return render(request, 'bets/bets_imprint.html')
