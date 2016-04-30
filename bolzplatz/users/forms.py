import logging

from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from .models import Profile

logger = logging.getLogger(__name__)

class UserCreationForm(BaseUserCreationForm):

    def clean_name(self):
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
            raise ValidationError("A user with that name already exists.")
        return username
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'slug': slugify(user.get_username()),
                })
        return user
