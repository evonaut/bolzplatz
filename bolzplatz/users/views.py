from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.utils.text import slugify

from .forms import UserCreationForm, GroupSelectForm
from .models import Profile, Group


class CreateAccount(View):
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:create_select_group')
    template_name = 'users/user_create.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(
            request,
            self.template_name,
            {'form': self.form_class()})

    @method_decorator(csrf_protect)
    @method_decorator(sensitive_post_parameters('password1', 'password2'))
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            if bound_form.save():
                group_select_url = reverse_lazy(
                    'auth:create_select_group',
                    kwargs={'slug': '{}'.format(bound_form.cleaned_data['username'])})
                return redirect(group_select_url)
            else:
                errs = (
                    bound_form.non_field_errors())
                for err in errs:
                    error(request, err)
                return redirect('auth:create')
        return TemplateResponse(
            request,
            self.template_name,
            {'form': bound_form})


class SelectGroup(View):
    form_class = GroupSelectForm
    success_url = reverse_lazy('auth:create_done')
    template_name = 'users/user_select_group.html'

    @method_decorator(csrf_protect)
    def get(self, request, slug):
        user = User.objects.get(username=slug)
        if user.is_active:
            return redirect('auth:login')
        return TemplateResponse(
            request,
            self.template_name,
            {'form': self.form_class(),
             'slug': slug})

    @method_decorator(csrf_protect)
    def post(self, request, slug):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            user = User.objects.get(username=slug)
            if user.is_active:
                return redirect('auth:login')
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'slug': slugify(user.get_username()),
                    'group': bound_form.cleaned_data['group'],
                })
            user.is_active = True
            user.save()

            return redirect('auth:create_done')

        return TemplateResponse(
            request,
            self.template_name,
            {'form': bound_form})
