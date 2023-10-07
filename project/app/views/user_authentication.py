from ..forms import PlayerSignUpForm, DungeonMasterSignUpForm
from ..models import User
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class PlayerSignUpView(UserPassesTestMixin, CreateView):
    model = User
    form_class = PlayerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['button'] = 'Sign Up'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

    def test_func(self):
        return not self.request.user.is_authenticated


class DungeonMasterSignUpView(UserPassesTestMixin, CreateView):
    model = User
    form_class = DungeonMasterSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['button'] = 'Sign Up'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

    def test_func(self):
        return not self.request.user.is_authenticated
