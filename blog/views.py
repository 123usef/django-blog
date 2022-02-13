from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blogApp/home.html')
def navbar(request):
    return render(request, 'blogApp/navbar.html')
def login(request):
    return render(request, 'blogApp/login.html')
def signup(request):
    return render(request, 'blogApp/signup.html')
