from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import User, Player, DungeonMaster


class PlayerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        Player.objects.create(user=user)
        return user


class DungeonMasterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dungeon_master = True
        user.save()
        DungeonMaster.objects.create(user=user)
        return user
