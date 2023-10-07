from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from app.views import user_authentication


def user_not_authenticated(user):
    return not user.is_authenticated


urlpatterns = [
    # path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),

    path('accounts/', include([
        path('', include('django.contrib.auth.urls')),
        path('signup/', user_passes_test(user_not_authenticated)(
            TemplateView.as_view(
                template_name='registration/choose_profile.html'
            )),
            name='signup'),
        path(
            'signup/player/',
            user_authentication.PlayerSignUpView.as_view(),
            name='player_signup'
        ),
        path(
            'signup/dungeon_master/',
            user_authentication.DungeonMasterSignUpView.as_view(),
            name='dungeon_master_signup'
        ),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),
]
