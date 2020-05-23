from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import menu_index, menu_details, menu_add, menu_details_uuid

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('menu:index')

        self.assertEqual(resolve(url).func, menu_index)

    def test_details_url_is_resolved(self):
        url = reverse('menu:details', args=['1'])

        self.assertEqual(resolve(url).func, menu_details)

    def test_add_url_is_resolved(self):
        url = reverse('menu:add')

        self.assertEqual(resolve(url).func, menu_add)

    def test_details_uuid_url_is_resolved(self):
        uuid = '49653d3c-9cb8-11ea-a730-6bbac3f29050'
        url = reverse('menu:details_uuid', args=[uuid])

        self.assertEqual(resolve(url).func, menu_details_uuid)
