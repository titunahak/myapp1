from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    dob = models.DateField()
    email = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)

    def __str__(self):
        return self.title