from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User , Post , Category


class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email","password1","password2"]
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', "post_content","cat_id","post_picture"]
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']


        

