from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm ,PostForm,CategoryForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Comment, Post, Reaction, Subscriptions, User, Category
from django.contrib import messages 
from django.http import HttpResponseRedirect
import requests
# Create your views here.


def base(request):
    return render(request, "blogApp/home.html")


def home(request):
    return render(request, "blogApp/home.html")


def post(request):
    return render(request, "blogApp/post.html")


def profile(request):
    return render(request, "blogApp/profile.html")


def useradmin(request):
    return render(request, 'blogApp/admin.html')
def createpost(request):
    return render(request, 'blogApp/createpost.html')
#register

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateForm()
        if request.method == "POST":
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(home)

        context = {"form": form}
        return render(request, "blogApp/register.html", context)

#login
def userlogin(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None :
                if user.user_status == 'unlocked':
                    login(request, user)
                    return redirect("homepage")
                else:
                    messages.error(request, "Your account is locked, please contact an admin.")
                    return redirect("login")      
            else:
                messages.error(request, "Username or passwoed is incorrecrt")
                return redirect("login")
        context = {}
        return render(request, "blogApp/login.html", context)

#logout
def userlogout(request):
    logout(request)
    return redirect("home")


# homepage view start
response = requests.get('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-02-16&'
       'sortBy=popularity&'
       'apiKey=b6ddcbd6ea8a4a418617efe10b23cb0c')
api_post = response.json()
ln = api_post["articles"]

def homepage(request):
    cats = Category.objects.all()
    posts = Post.objects.all()
   
    if request.user.is_authenticated:
        return redirect("user_subscriptions")

    context = {"cats": cats, "posts": posts ,  "ln":ln }
    return render(request, "blogApp/homepage.html", context)


# class categoryview(ListView):
#     model = Category
#     template_name = 'homepage.html'

# categories

#category
def det_category(request, id):
    category = Category.objects.get(id=id)
    cats = Category.objects.all()
    user = request.user
    if request.user.is_authenticated:
        subs = user.subscriptions_set.all()
    
    posts = category.post_set.all().order_by("-post_cr_date")
    context = {"posts": posts, "cats": cats}

    return render(request, "blogApp/homepage.html", context)


# subscriptions
def user_subscriptions(request):
    cats = Category.objects.all()
    user = request.user
    subs = user.subscriptions_set.all()
    subs_id = []
    for sub in subs:
        subs_id.append(sub.cat_id)
    if len(subs) == 0:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(cat_id__in=subs_id)
    context = {"posts": posts, "cats": cats, "subs_id": subs_id,"ln":ln}
    return render(request, "blogApp/homepage.html", context)


def subscribe(request, id):
    user_id = request.user.id
    category = Category.objects.get(id=id)
    subscribe = Subscriptions.objects.create(user_id=request.user, cat_id=category)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unsubscribe(request, id):
    user_id = request.user.id
    category = Category.objects.get(id=id)
    subscribe = Subscriptions.objects.get(user_id=request.user, cat_id=category)
    subscribe.delete()
    print(5)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# post
def det_post(request, id):
    post = Post.objects.get(id=id)
    reacts = post.reaction_set.all()
    likes = len(reacts.filter(reaction="like"))
    dislikes = len(reacts.filter(reaction="dislike"))
    comment = Comment.objects.filter(post_id=id).order_by("-cmnt_cr_date")
    reaction = Reaction.objects.filter(post_id=id)
    context = {
        "post": post,
        "comment": comment,
        "reaction": reaction,
        "likes": likes,
        "dislikes": dislikes,
    }
    return render(request, "blogApp/postdetails.html", context)


def add_reaction(request, id, react):
    user = request.user
    post = Post.objects.get(id=id)
    reaction = Reaction.objects.create(post_id=post, user_id=user, reaction=react)
    return redirect("post", id=id)


# search method
def search(request):
    if request.method == "GET":
        user_value = request.GET.get("search_value")
        result = Post.objects.all().filter(post_title__contains=user_value)
        context = {"post": result}
        return render(request, "blogApp/search_results.html", context)
    
#admin_list_all_posts
def list_post(request):
        all_posts = Post.objects.all() 
        context = { "posts" : all_posts }
        return render(request, "blogApp/admin.html", context)
def list_users(request):
        all_users = User.objects.all()   
        context = { "users" : all_users }
        return render(request, "blogApp/admin.html", context)

def list_categories(request):
        all_categories = Category.objects.all()   
        context = { "categories" : all_categories }
        return render(request, "blogApp/admin.html", context)

#locked user
def locked(request, id):
    userlock = User.objects.get(id = id)
    userlock.user_status = 'locked'
    userlock.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unlocked(request, id):
    userlock = User.objects.get(id = id)
    userlock.user_status = 'unlocked'
    userlock.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#post crud   

def updatepost(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        form = PostForm(request.POST ,instance=post )
        if form.is_valid():
            form.save()
            return redirect('list_post')
        
    form = PostForm(instance = post)
    context = {'form' : form} 
    return render(request, 'blogApp/updatepost.html' , context)
def updatecategory(request, id):
    category = Category.objects.get(id = id)
    if request.method == 'POST':
        form = CategoryForm(request.POST ,instance=category )
        if form.is_valid():
            form.save()
            return redirect('list_categories')
        
    form = CategoryForm(instance = category)
    context = {'form' : form} 
    return render(request, 'blogApp/updatecategory.html' , context)
    
def deletepost( request, id ):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('list_post')
#category crud  
def deletecategory( request, id ):
    category = Category.objects.get(id = id)
    category.delete()
    return redirect('list_categories')
      
    

    

