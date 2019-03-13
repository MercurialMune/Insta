from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Profile
from. forms import UploadForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()

    return render(request, 'welcome.html', locals())


@login_required(login_url='/accounts/login')
def userspace(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()

    return render(request, 'profile.html', locals())


def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.save()
            return redirect('welcome')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'uploadform':form})


