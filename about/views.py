from django.shortcuts import render

# Create your views here.
def about_us(request):
    template_name = "about/about_us_copy.html"
    return render(request, template_name)