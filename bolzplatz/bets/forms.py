from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user

from .models import Bet, Match

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['match', 'score_home', 'score_visitor']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BetForm, self).__init__(*args, **kwargs)

    def clean_match(self):
        match = self.cleaned_data['match']
        if Bet.objects.filter(match=match, user=self.user).exists():
            raise ValidationError('Du hast für dieses Spiel schon einen Tipp abgegeben!')
        return match

    def save(self, request, commit=True):
        bet = super().save(commit=False)
        if not bet.pk:
            bet.user = get_user(request)
        if commit:
            bet.save()
            return bet


