from blog.models import Category, Blog
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request, ):
    blogs = Blog.objects.all()
    category = Category.objects.all()
    images = Category.objects.all()
    context = {'blogs': blogs,
               'category': category,
               'imagess': images,
             }
    return render(request, 'blogs.html', context)



