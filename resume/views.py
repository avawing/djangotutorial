from django.shortcuts import render
from .models import Resume, Post

# Create your views here.


def home(request):
    return render(request, 'resume/home.html')


def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {'resume':resume})


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'resume/blog.html', context)