from django import forms
from .models import Menu, Option

class MenuForm(forms.ModelForm):
    """
    Defines Menu fields
    """

    class Meta:
        model = Menu
        fields = ['published_date']
