from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.template.context_processors import request

from accounts.forms import RegistrationForm

# Create your views here.

def register_view(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    # manage info sent through the form, using POST REQUEST
    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    else:
        return HTTPResponse(form.errors)

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')
    else:
        return HTTPResponse(form.errors)