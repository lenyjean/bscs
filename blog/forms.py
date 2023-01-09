from django import forms
from .models import *

class BlogPostForms(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your story here'}))
    
    class Meta: 
        model = BlogPost
        fields = [
            'title', 'about_blog', 'category', 'image', 'content', 'status', 
        ]
        widgets = {
            'content' : forms.Textarea(attrs={
                'maxlength': '200'
            }),
        }