from django import forms
from .models import *

class BlogPostForms(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your story here'}))
    
    class Meta: 
        model = BlogPost
        fields = [
            'title', 'description', 'category', 'image', 'content', 'status', 
        ]
        widgets = {
            'content' : forms.Textarea(attrs={
                'maxlength': '200'
            }),
        }