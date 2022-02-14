from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Post, Subscriptions, User, Category

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateForm()
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(homepage)

        context = {'form': form}
        return render(request, "blogApp/signup.html", context)

      
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password) 
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else :
                return redirect('register')          
        context={}
        return render(request,'blogApp/login.html',context)


def userlogout(request):
	logout(request)
	return redirect('homepage')

# homepage view start

def navbar(request):
    return render(request, 'blogApp/navbar.html')
def homepage(request):
    cats = Category.objects.all()
    posts = Post.objects.all()  
    if request.user.is_authenticated:
        return redirect('user_subscriptions')
  
    context = {'cats': cats, 'posts': posts}
    return render(request, 'blogApp/homepage.html', context)

class categoryview(ListView):
    model = Category
    template_name = 'homepage.html'

# categories

def det_category(request,id):
    category = Category.objects.get(id=id)
    cats = Category.objects.all()
    posts = category.post_set.all().order_by('-post_cr_date')
    context = {'posts' : posts, 'cats' : cats}
    return render(request, 'blogApp/homepage.html', context)

# subscriptions

def user_subscriptions(request):
    cats = Category.objects.all()
    user = request.user
    subs = user.subscriptions_set.all()
    subs_id = []
    for sub in subs:
       subs_id.append(sub.cat_id)
    posts = Post.objects.filter(cat_id__in = subs_id)
    context = {'posts' : posts, 'cats' : cats}
    return render(request, 'blogApp/homepage.html', context)


def subscribe(request,id):
    user_id = request.user.id
    category = Category.objects.get(id=id)
    subscribe = Subscriptions.objects.create(user_id = request.user, cat_id = category)
    return redirect(user_subscriptions)




