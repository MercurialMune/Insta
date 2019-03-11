from django.shortcuts import render
from .models import Image, Profile


def welcome(request):
    return render(request, 'welcome.html')


def gallery(request):
    all_locations = Profile.objects.all()
    images = Image.objects.all()
    return render(request, 'categories/all-images.html', {"all_locations": all_locations, "images": images})
