from django.db import models

# Create your models here.
from django.db import models
from django import forms


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10, choices=(('employee', 'Employee'), ('staff', 'Staff')))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, label='Email')
    password = forms.CharField(max_length=128, label='Password', widget=forms.PasswordInput())
