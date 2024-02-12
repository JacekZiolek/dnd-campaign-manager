from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "is_player",
            "is_dungeon_master",
            "username",
            "email",
            "password1",
            "password2",
        )

        widgets = {
            "is_player": forms.RadioSelect(),
            "is_dungeon_master": forms.RadioSelect(),
        }
