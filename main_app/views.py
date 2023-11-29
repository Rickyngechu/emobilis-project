from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from main_app.models import UserForm, LoginForm


# Create your views here.
def home(request):
    return render(request, "index.html")


# @login_required
def resources(request):
    return render(request, "resources.html")


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('email', 'Invalid email or password')

    context = {'form': form}
    return render(request, 'login.html', context)
