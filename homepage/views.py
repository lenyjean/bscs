from django.shortcuts import render, redirect
from .forms import *
from blog.models import *
# Create your views here.
def homepage(request):
    template_name = 'homepage/homepage.html'
    blog_post = BlogPost.objects.filter(status__in=["Publish"])[:4]   
    context = {
        "blog_post" : blog_post
    }
    return render(request, template_name, context)

def home_blog_detail(request, pk):
    template_name = "homepage/blog_detail.html"
    blog_post = BlogPost.objects.filter(id=pk)
    context = {
        "blog_post": blog_post
    }
    return render(request, template_name, context)