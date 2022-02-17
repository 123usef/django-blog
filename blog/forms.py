from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, User


class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email","password1","password2"]

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title','post_picture','post_content','cat_id']
