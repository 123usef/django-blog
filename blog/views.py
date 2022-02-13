from venv import create
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm
from django.contrib.auth import authenticate, login, logout

# from .forms import CreateForm

from .models import User
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateForm()
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home.html')

        context = {'form': form}
        return render(request, "register.html", context)

    

