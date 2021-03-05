from django.db import models

# Create your models here.


class Resume(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    freelance = models.CharField(max_length=30, default="Available")
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    languages = models.CharField(max_length=30)