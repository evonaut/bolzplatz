from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse

class CreateAccount(View):
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:create_done')
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
                return redirect(self.success_url)
            else:
                errs = (
                    bound_form.non_field_errors())
                for err in errs:
                    error(request, err)
                return redirect(
                    'auth:create')
        return TemplateResponse(
            request,
            self.template_name,
            {'form': bound_form})