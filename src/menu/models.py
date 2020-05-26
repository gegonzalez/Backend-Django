from django.db import models

class Menu(models.Model):
    """
    Defines the Menu data fields
    """
    uuid           = models.CharField(max_length=50, default="")
    published_date = models.CharField(max_length=10, unique=True)

class Option(models.Model):
    """
    Defines the Option data fields
    """
    uuid        = models.CharField(max_length=50, default="")
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="options")
    description = models.CharField(max_length=250, default="")

class Order(models.Model):
    """
    Defines the Order data fields
    """
    option        = models.ForeignKey(Option, on_delete=models.PROTECT)
    uuid          = models.CharField(max_length=50, default="")
    name          = models.CharField(max_length=250, default="")
    customization = models.CharField(max_length=250, default="")
