import logging

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Profile, Group


class UserCreationForm(BaseUserCreationForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = (
            'activate',
            'create',
            'disable',
            'login',
            'logout',
            'password',
            'profile',
        )
        if username in disallowed:
            raise ValidationError(_('A user with that name already exists.'))
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_active = False
            user.save()
        return user


class GroupSelectForm(forms.Form):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all().order_by('slug'))

    def clean_group(self):
        group = self.cleaned_data['group']
        if not group:
            raise ValidationError(_('Please select a group.'))
        return group
