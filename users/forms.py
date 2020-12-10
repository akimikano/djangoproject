from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post
from django.forms import ModelForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # code_word = forms.CharField(max_length=40)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class MakePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
