from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    redirect_authenticated_user = True      # didin't work
    success_url = reverse_lazy('accounts_app:done_login')
    def form_valid(self, form):
        print('ran here 2----')
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    def form_invalid(self, form):
        print('invalid form----')
        errors = form.errors.as_data()
        print(errors)
        invalid_fields = list(errors.keys())
        print(invalid_fields)
        return HttpResponse('invalid form')
    
    def get(self, *args, **kwargs):     # an already logged in user will be redirected
        if self.request.user.is_authenticated:
            return redirect('accounts_app:done_login')
        return super(RegisterView, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True   # an already logged in user will be redirected

    def get_success_url(self):
        return reverse_lazy('accounts_app:done_login')


@login_required()
def login_success_index(request):
    return HttpResponse('login_success')