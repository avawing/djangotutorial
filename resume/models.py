from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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


class Post(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Form(models.Model):
    your_name = models.CharField(max_length=20)
    your_email = models.CharField(max_length=30)
    your_subject = models.CharField(max_length=30)
    your_message = models.TextField()