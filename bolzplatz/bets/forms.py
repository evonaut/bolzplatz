from django import forms
from django.contrib.auth import get_user

from .models import Bet, Match

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['match', 'score_home', 'score_visitor']

    def save(self, request, commit=True):
        bet = super().save(commit=False)
        if not bet.pk:
            bet.user = get_user(request)
        if commit:
            bet.save()
            return bet


