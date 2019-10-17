from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse

from .models import Post, User
from .forms import UploadImageForm


def home(request):
    latest_pictures = Post.objects.all()
    context = {'latest_pictures': latest_pictures}
    return render(request, 'home/home.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UploadImageForm(request.POST, request.FILES)
    return render(request, 'upload/upload.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form':form})


def myimages(request):
    my_pictures = Post.objects.filter(user=request.user)
    context = {'my_pictures': my_pictures}
    return render(request, 'myimages/myimages.html', context)



