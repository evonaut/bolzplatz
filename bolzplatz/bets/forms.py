from django import forms

from .models import Bet, Match

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['match', 'score_home', 'score_visitor']
