from django.urls import path
from .views import *

urlpatterns = [
    path('blog-list', blog_list, name='blog-list'),
    path('create-your-blog', add_blog, name='create-your-blog'),
    path('blog-detail/<int:pk>', blog_detail, name='blog-detail'),
    path('update-your-blog/<int:pk>', update_blog, name='update-your-blog'),
    path('delete-your-blog/<int:pk>', delete_blog, name='delete-your-blog'),
  
  
]
