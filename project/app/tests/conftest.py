import pytest
from faker import Faker
from django.test import Client, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from ..models import User, Player, DungeonMaster

faker = Faker()


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def request_factory():
    request_factory = RequestFactory()
    return request_factory


@pytest.fixture
def middleware():
    middleware = SessionMiddleware(lambda x: None)
    return middleware


@pytest.fixture
def user():
    user = User.objects.create(
        username=faker.name(),
        email=faker.email(),
        password=faker.password()
    )
    return user


@pytest.fixture
def player(user):
    user.is_player = True
    player = Player.objects.create(user=user)
    return player


@pytest.fixture
def dungeon_master(user):
    user.is_dungeon_master = True
    dungeon_master = DungeonMaster.objects.create(user=user)
    return dungeon_master
