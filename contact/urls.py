from django.urls import path
from .views import *

urlpatterns = [
    path('contact-us', contact, name='contact-us'),
    path('contact-success', contact_success, name='contact-success'),
    path('success', success, name='success'),
    path('contact-list', contact_list, name='contact-list'),
    path('add-contact', contact_add, name='add-contact'),
    path('contact-detail', contact_detail, name='contact-detail'),
]
