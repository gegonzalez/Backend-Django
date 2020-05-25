from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from menu.views import (menu_index, menu_add, option_add, option_edit)

class TestViews(TestCase):
    EXPECTED_OK_STATUS_CODE = 200
    EXPECTED_REDIRECT_STATUS_CODE = 302
    EXPECTED_NOT_FOUND_STATUS_CODE = 404
    UUID = '49653d3c-9cb8-11ea-a730-6bbac3f29050'

    def test_menu_index_login_required(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()

        response = menu_index(request)

        self.assertEqual(response.status_code, self.EXPECTED_REDIRECT_STATUS_CODE)

    def test_menu_index_is_callable(self):
        request = RequestFactory().get('/')
        request.user = User()

        response = menu_index(request)
        self.assertEqual(response.status_code, self.EXPECTED_OK_STATUS_CODE)

    def test_menu_add_login_required(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()

        response = menu_add(request)

        self.assertEqual(response.status_code, self.EXPECTED_REDIRECT_STATUS_CODE)

    def test_menu_add_is_callable(self):
        request = RequestFactory().get('/')
        request.user = User()

        response = menu_add(request)

        self.assertEqual(response.status_code, self.EXPECTED_OK_STATUS_CODE)

    def test_menu_add_is_callable_with_post(self):
        data = {'foo': 'bar'}
        request = RequestFactory().post('/', data)
        request.user = User()

        response = menu_add(request)

        self.assertEqual(response.status_code, self.EXPECTED_OK_STATUS_CODE)

    def test_option_add_login_required(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()

        response = option_add(request, self.UUID)

        self.assertEqual(response.status_code, self.EXPECTED_REDIRECT_STATUS_CODE)

    def test_option_add_is_callable(self):
        request = RequestFactory().get('/')
        request.user = User()

        response = option_add(request, self.UUID)

        self.assertEqual(response.status_code, self.EXPECTED_OK_STATUS_CODE)

    def test_option_add_is_callable_with_post(self):
        data = {'foo': 'bar'}
        request = RequestFactory().post('/', data)
        request.user = User()

        response = option_add(request, self.UUID)

        self.assertEqual(response.status_code, self.EXPECTED_OK_STATUS_CODE)

    def test_option_edit_login_required(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()

        response = option_edit(request, self.UUID)

        self.assertEqual(response.status_code, self.EXPECTED_REDIRECT_STATUS_CODE)
