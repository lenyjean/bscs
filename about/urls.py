from django.urls import path
from .views import *

urlpatterns = [
    path('about-us', about_us, name='about-us'),
]
