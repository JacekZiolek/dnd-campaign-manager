from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView


class ProfileView(UserPassesTestMixin, TemplateView):
    template_name = "profile.html"

    def test_func(self):
        return self.request.user.is_authenticated
