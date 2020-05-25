from django import forms

class MenuForm(forms.Form):
    """
    Defines Menu fields
    """
    publishedDateInput = forms.CharField(max_length=250)

class OptionForm(forms.Form):
    """
    Defines Option fields
    """
    description = forms.CharField(max_length=250)

class OrderForm(forms.Form):
    """
    Defines Order fields
    """
    name          = forms.CharField(max_length=250)
    customization = forms.CharField(max_length=250)
