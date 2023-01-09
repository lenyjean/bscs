from django import forms
from .models import *

class ContactForms(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message here'}))
    your_name = forms.CharField(max_length=255, label="Enter your full name")
    your_email = forms.EmailField(max_length=255, label="Enter your email (example@gmail.com)")
    subject = forms.CharField(max_length=255, label="Subject")
    address =  forms.CharField(max_length=255, label="Enter your address")
    phone = forms.CharField(max_length=255, label="Enter your phone number (e.g +63 9652351921)")


    class Meta: 
        model = ContactModel
        fields = [
            'your_name', 'phone', 'address', 'your_email', 'subject', 'message' 
        ]
        