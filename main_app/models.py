from django.db import models

# Create your models here.
from django.db import models
from django import forms


class Resource(models.Model):
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10, choices=(('staff', 'Developer'), ('staff', 'User')))

    def __str__(self):
        return self.username


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='username')
    password = forms.CharField(max_length=128, label='Password', widget=forms.PasswordInput())


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# class DeveloperResource(models.Model)
