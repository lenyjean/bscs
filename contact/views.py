from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def contact(request):
    template_name = "contact_us/contact_us.html"
    return render(request, template_name)

def contact_success(request):
    if request.method == 'POST':
        your_name = request.POST['name']
        phone = request.POST['phone']
        your_email = request.POST['email']
        address = request.POST['address']
        subject = request.POST['subject']
        message = request.POST['message']
        data = ContactModel(your_name=your_name,phone=phone,address=address,your_email=your_email,subject=subject,message=message)
        data.save()
        return redirect('success.html')
    else:
        return render(request,'contact_us/contact_us.html')
        
def success(request):
    template_name = 'contact_us/success.html'
    contact = ContactModel.objects.all()
    contact.save()
    return render(request, template_name)


def contact_list(request):
    template_name = "contact_us/contact_list.html"
    return render(request, template_name)

def contact_detail(request, pk):
    template_name = "contact_us/contact_detail.html"
    contact =  ContactModel.objects.filter(id=pk)   
    context = {
        'contact': contact
    }
    return render(request, template_name, context)

def contact_add(request):
    template_name = "contact_us/add_contact.html"
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("contact-us")
    context = {
        'form': form
    }
    return render(request, template_name, context)
