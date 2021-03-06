from django.contrib import admin

# Register your models here.
from .models import Resume, Post

admin.site.register(Resume)
admin.site.register(Post)