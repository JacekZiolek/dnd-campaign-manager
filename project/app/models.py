from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_player = models.BooleanField(default=False)
    is_dungeon_master = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", default="profile_pictures/default.png"
    )
    email = models.EmailField(
        unique=True, error_messages={"unique": "This email has already been taken."}
    )


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class DungeonMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
