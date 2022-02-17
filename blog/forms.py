
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User , Post , Category


class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email","password1","password2"]

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title','post_picture','post_content','cat_id']
        widgets = {
            'post_title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            'post_content' :forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
            }

             # 'post_picture' : forms.ImageField(),attrs={
                #     'class':'form-control'
                # }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', "post_content","cat_id","post_picture"]
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']


        

