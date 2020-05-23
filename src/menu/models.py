from uuid import uuid1
from django.db import models


class Menu(models.Model):
    """
    Defines the Menu data fields
    """
    uuid           = models.CharField(max_length=36, default="")
    published_date = models.DateField(unique=True)

    def save(self, *args, **kwargs):
        self.uuid = uuid1()
        super(Menu, self).save(*args, **kwargs)

class Option(models.Model):
    """
    Defines the Option data fields
    """
    menu        = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
