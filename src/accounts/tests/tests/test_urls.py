from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import signup_view, login_view

class TestUrls(SimpleTestCase):

    def test_signup_url_is_resolved(self):
        url = reverse('accounts:signup')

        self.assertEqual(resolve(url).func, signup_view)

    def test_login_url_is_resolved(self):
        url = reverse('accounts:login')

        self.assertEqual(resolve(url).func, login_view)
