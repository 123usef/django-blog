from venv import create
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm
from django.contrib.auth import authenticate, login, logout

# from .forms import CreateForm

from .models import User
# Create your views here.


def home(request):
    return render(request, 'blogApp/home.html')
def navbar(request):
    return render(request, 'blogApp/navbar.html')
def homepage(request):
    return render(request, 'blogApp/homepage.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateForm()
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(home)

        context = {'form': form}
        return render(request, "blogApp/signup.html", context)

      
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password) 
            if user is not None:
                login(request,user)
                return redirect('home')
            else :
                return redirect('register')          
        context={}
        return render(request,'blogApp/login.html',context)


def userlogout(request):
	logout(request)
	return redirect('nav')