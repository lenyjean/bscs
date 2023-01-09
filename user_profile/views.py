from django.shortcuts import render

# Create your views here.
def profile(request):
    template_name = 'user_profile/profile_list.html'
    return(request, template_name)