from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post

        exclude = ['user']