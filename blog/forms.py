from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email", "user_status", "user_role"]
