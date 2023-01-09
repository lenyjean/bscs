from django.urls import path


from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("detail/<int:pk>", home_blog_detail, name="detail")
]