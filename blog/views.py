from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.core.paginator import Paginator



def home(request):
    template_name = 'blog/home.html'
    return render(request, template_name)

def blog_list(request):
    # template_name = "blog/list copy.html"
    blog_post = BlogPost.objects.all().order_by('id')
    paginator = Paginator(blog_post, 3 )

    page_number = request.GET.get('page')
    blog_post = paginator.get_page(page_number)

    return render(request, 'blog/list_copy.html', {'page_obj': blog_post})
    # blog_post = BlogPost.objects.filter(status__in=['Publish', 'Draft'])
    # context = {
    #     'blog_post': blog_post,
    # }
    # return render (request, template_name, context)

def blog_detail(request, pk):
    template_name = 'blog/blog_detail.html'
    blog_post = BlogPost.objects.filter(id=pk)   
    context = {
        'blog_post': blog_post
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def add_blog(request):
    template_name = 'blog/add_blog.html'
    form = BlogPostForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author_id = request.user.id
        blog.save()
        return redirect("blog-list")
    context = {
        'form': form
    }
    return render(request, template_name, context)

def update_blog(request, pk):
    template_name = 'blog/update_blog.html'
    blog_post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForms(request.POST or None, instance=blog_post)
    if form.is_valid():
        form.save()
        return redirect("blog-list")
    context = {
        "form":  form
    }
    return render(request, template_name, context)

def delete_blog(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    blog_post.delete()
    return redirect("blog-list")


