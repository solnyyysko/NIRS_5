from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from app.forms import LoginForm, RegistrationForm


def index(request):
    return render(request, 'index.html')


def login(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'GET':
        user_form = LoginForm()
    if request.method == 'POST':
        user_form = LoginForm(data=request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request, **user_form.cleaned_data)
            if user:
                return redirect(reverse("index"))
            else:
                user_form.add_error(field=None, error="Wrong username or password!")
    return render(request, 'login.html', {'form': user_form})


def registration(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                return redirect(reverse("index"))
            else:
                user_form.add_error(field=None, error="User saving error!")
    return render(request, 'registration.html', {'form': user_form})


def ticket(request):
    return render(request, 'ticket.html')


def order(request):
    return render(request, 'order.html')
