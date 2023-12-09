import pytest
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from ..views.user_authentication import SignUpView


@pytest.mark.django_db
def test_player_signup(client):
    response = client.get(reverse('player_signup'))
    assert response.status_code == 302
    assert response.url == '/accounts/signup/'

    response = client.post(reverse('player_signup'))
    assert response.status_code == 200
    assert client.session['user_type'] == 'player'


@pytest.mark.django_db
def test_dungeon_master_signup(client):
    response = client.get(reverse('dungeon_master_signup'))
    assert response.status_code == 302
    assert response.url == '/accounts/signup/'

    response = client.post(reverse('dungeon_master_signup'))
    assert response.status_code == 200
    assert client.session['user_type'] == 'dungeon_master'


@pytest.mark.django_db
def test_SignUpView(request_factory, middleware, player, dungeon_master):
    def make_request(method, user_type=None):
        request = request_factory.generic(method, reverse('signup'))
        request.user = AnonymousUser()
        middleware.process_request(request)
        if user_type:
            request.session['user_type'] = user_type
        request.session.save()
        return request

    view = SignUpView.as_view()

    request = make_request('GET')
    response = view(request)
    assert response.status_code == 200

    request = make_request('GET')
    request.user = player.user
    with pytest.raises(PermissionDenied):
        response = view(request)

    request = make_request('GET')
    request.user = dungeon_master.user
    with pytest.raises(PermissionDenied):
        response = view(request)

    request = make_request('POST', 'player')
    response = view(request)
    assert response.status_code == 200
    assert 'user_type' in request.session
    assert request.session['user_type'] == 'player'

    request = make_request('POST', 'dungeon_master')
    response = view(request)
    assert response.status_code == 200
    assert 'user_type' in request.session
    assert request.session['user_type'] == 'dungeon_master'
