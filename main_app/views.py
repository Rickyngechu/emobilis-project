from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from main_app.models import UserForm, LoginForm, Bookmark, Resource


# Create your views here.
def home(request):
    return render(request, "index.html")


@login_required
def resources(request):
    return render(request, "resources.html")


def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logacc')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def logacc(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('resources')
            else:
                form.add_error('password', 'Invalid email or password')

    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def logout(request):
    logout(request)
    return redirect('signup')


def user(request):
    return render(request, 'user.html')


@login_required
def list_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookmarks/list.html', {'bookmarks': bookmarks})


@login_required
def add_bookmark(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    Bookmark.objects.create(user=request.user, resource=resource)
    return redirect('list_bookmarks')


@login_required
def remove_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if bookmark.user == request.user:
        bookmark.delete()
    return redirect('list_bookmarks')
