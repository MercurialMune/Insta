from django.shortcuts import render, HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Profile, Users
from. forms import RegistrationForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    all_locations = Profile.objects.all()
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"all_locations": all_locations, "images": images})


def user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Users(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            print(recipient)
            HttpResponseRedirect('user')
    else:
        form = RegistrationForm()
    return render(request, 'another.html', {'regform':form})


@login_required(login_url='/accounts/login/')
def gallery(request):
    all_locations = Profile.objects.all()
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"all_locations": all_locations, "images": images})
