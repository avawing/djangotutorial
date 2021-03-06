from django.contrib import admin

# Register your models here.
from .models import Resume, Post, Form

admin.site.register(Resume)
admin.site.register(Post)
admin.site.register(Form)