from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..forms import SignUpForm
from ..models import DungeonMaster, Player, User


def player_signup(request):
    if request.method == "GET":
        return redirect("/accounts/signup/")
    if request.method == "POST":
        request.session["user_type"] = "player"
        form = SignUpForm()
        ctx = {
            "form": form,
            "btn": "Sign Up As Player",
            "session": request.session["user_type"],
        }
        return render(request, "registration/signup_form.html", ctx)


def dungeon_master_signup(request):
    if request.method == "GET":
        return redirect("/accounts/signup/")
    if request.method == "POST":
        request.session["user_type"] = "dungeon_master"
        form = SignUpForm()
        ctx = {
            "form": form,
            "btn": "Sign Up As Dungeon Master",
            "session": request.session["user_type"],
        }
        return render(request, "registration/signup_form.html", ctx)


class SignUpView(UserPassesTestMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user_type = self.request.session["user_type"]
        user = form.save(commit=False)
        user.is_player = user_type == "player"
        user.is_dungeon_master = user_type == "dungeon_master"
        user.save()
        if user.is_player:
            Player.objects.create(user=user)
        if user.is_dungeon_master:
            DungeonMaster.objects.create(user=user)
        login(self.request, user)
        return redirect("/")

    def test_func(self):
        return not self.request.user.is_authenticated
