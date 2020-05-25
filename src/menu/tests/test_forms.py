from django.test import TestCase

from menu.forms import MenuForm, OptionForm, OrderForm

class TestForms(TestCase):

    def test_menu_form_valid(self):

        form = MenuForm(data={'publishedDateInput': '2020-31-12'})

        self.assertTrue(form.is_valid())

    def test_menu_form_invalid(self):

        form = MenuForm(data={'publishedDateInput': ''})

        self.assertFalse(form.is_valid())

    def test_option_form_valid(self):

        form = OptionForm(data={'description': 'dummy description'})

        self.assertTrue(form.is_valid())

    def test_option_form_invalid(self):

        form = OptionForm(data={'description': ''})

        self.assertFalse(form.is_valid())

    def test_order_form_valid(self):

        form = OrderForm(data={'name': 'dummy name', 'customization': 'dummy customization'})

        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):

        form = OrderForm(data={'name': 'dummy name'})

        self.assertFalse(form.is_valid())
