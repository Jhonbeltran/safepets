""" Post models """
from django.db import models

class Users(models.Model):
    """ Post Users """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    is_admin = models.BooleanField(default=False)

    birth_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
