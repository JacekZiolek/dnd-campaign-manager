from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from app.views import user_authentication, profile


def user_not_authenticated(user):
    return not user.is_authenticated


urlpatterns = [
    # path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),

    path('accounts/', include([
        path('', include('django.contrib.auth.urls')),
        path('signup/', user_passes_test(user_not_authenticated)(
            user_authentication.SignUpView.as_view()),
            name='signup'),
        path(
            'signup/player/',
            user_authentication.player_signup,
            name='player_signup'
        ),
        path(
            'signup/dungeon_master/',
            user_authentication.dungeon_master_signup,
            name='dungeon_master_signup'
        ),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('profile/', profile.ProfileView.as_view(), name='profile'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
