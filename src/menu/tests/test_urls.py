from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import menu_index, menu_add, menu_details_uuid, option_add, option_edit
from menu.views import menu_order, order_add, order_details, order_index

class TestUrls(SimpleTestCase):
    UUID = '49653d3c-9cb8-11ea-a730-6bbac3f29050'

    def test_index_url_is_resolved(self):
        url = reverse('menu:index')

        self.assertEqual(resolve(url).func, menu_index)

    def test_add_url_is_resolved(self):
        url = reverse('menu:add')

        self.assertEqual(resolve(url).func, menu_add)

    def test_details_uuid_url_is_resolved(self):
        url = reverse('menu:details_uuid', args=[self.UUID])

        self.assertEqual(resolve(url).func, menu_details_uuid)

    def test_option_add_url_is_resolved(self):
        url = reverse('menu:option_add', args=[self.UUID])

        self.assertEqual(resolve(url).func, option_add)

    def test_option_edit_url_is_resolved(self):
        url = reverse('menu:option_edit', args=[self.UUID])

        self.assertEqual(resolve(url).func, option_edit)

    def test_menu_order_url_is_resolved(self):
        url = reverse('menu:order', args=[self.UUID])

        self.assertEqual(resolve(url).func, menu_order)

    def test_order_add_url_is_resolved(self):
        url = reverse('menu:order_add', args=[self.UUID])

        self.assertEqual(resolve(url).func, order_add)

    def test_order_details_url_is_resolved(self):
        url = reverse('menu:order_details', args=[self.UUID])

        self.assertEqual(resolve(url).func, order_details)

    def test_order_index_url_is_resolved(self):
        url = reverse('menu:order_index')

        self.assertEqual(resolve(url).func, order_index)
