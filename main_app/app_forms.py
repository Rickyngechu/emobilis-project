from django import forms

from main_app.models import User, Resource


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
