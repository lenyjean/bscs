from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=255, label="Your Name")
    email = forms.EmailField(max_length=255, label="Your Email")
    message = forms.CharField(max_length=1000,widget=forms.Textarea)