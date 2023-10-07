from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_player = models.BooleanField(default=False)
    is_dungeon_master = models.BooleanField(default=False)


class Player(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class DungeonMaster(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
