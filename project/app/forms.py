from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    profile_type = forms.ChoiceField(
        choices=(("is_player", "Player"), ("is_dungeon_master", "Dungeon Master")),
        widget=forms.RadioSelect(),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
