from django.http import HttpResponse
from django.shortcuts import render
from django.utils import translation
from django.conf import settings
from ico.settings import PARLER_LANGUAGES
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all()

    context = {
       'blogs': blogs 
    }
    return render(request, 'home.html', context)

def profile(request):

    return render(request, 'profile.html')

def has_acces():
    return True

