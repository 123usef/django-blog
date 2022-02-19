# from curses import meta
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateForm ,PostForm,CategoryForm,CreatePost
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .models import Comment, Post, Reaction, Subscriptions, User, Category
from django.contrib import messages 
from django.http import HttpResponseRedirect
import requests

# import pagination
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.paginator import Paginator
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

# def pagination(request):
#     return render(request, 'blogApp/footer.html')

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
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None :
                if user.user_status == 'unlocked':
                    login(request, user)
                    return redirect("home")
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
    user = request.user
    cats = Category.objects.all()
    posts = Post.objects.all()
    # subs = user.subscriptions_set.all()
    if request.user.is_authenticated:
         subs = user.subscriptions_set.all()
         return redirect("user_subscriptions")
# context = {"cats": cats, "posts": posts ,"subs": subs ,"ln":ln }
    context = {"cats": cats, "posts": posts ,"ln":ln }
    return render(request, "blogApp/homepage.html", context)


# search method

def search(request):
    if request.method == "GET":
        user_value = request.GET.get("search_value")
        result = Post.objects.all().filter(post_title__contains=user_value)
        context = {"post": result}
        return render(request, "blogApp/search_results.html", context)

#category
def det_category(request, id):
    category = Category.objects.get(id=id)
    cats = Category.objects.all()
    user = request.user
    if request.user.is_authenticated:
        subs = user.subscriptions_set.all()
    
    posts = category.post_set.all().order_by("post_cr_date")
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
    context = {"posts": posts, "cats": cats, "subs_id": subs_id,"ln":ln, "subs":subs}
    return render(request, "blogApp/homepage.html", context)

#subscribe
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


# Post

def det_post(request, id):
    post = Post.objects.get(id=id)
    reacts = post.reaction_set.all()
    likes = len(reacts.filter(reaction="like"))
    dislikes = len(reacts.filter(reaction="dislike"))
    comment = Comment.objects.filter(post_id=id).order_by("-cmnt_cr_date")
    reaction = Reaction.objects.filter(post_id=id)
    context = {
        "post": post,
        "comments": comment,
        "reaction": reaction,
        "likes": likes,
        "dislikes": dislikes,
    }
    return render(request, "blogApp/postdetails.html", context)

#create post 

def create_post(request):
    # user = request.user
    # form = CreatePost()
    if request.method == "POST":
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            sv=form.save(commit=False)
            sv.user_id_id=request.user.id
            sv.save()
            return redirect ('homepage')
    else:
        form = CreatePost()
        
  
    context = {'form': form}
    return render (request, 'blogApp/create_post.html', context) 


# Reactions

#add reaction
def add_reaction(request, id, react):
    user = request.user
    post = Post.objects.get(id=id)
    reaction_existed = Reaction.objects.filter(post_id=post, user_id=user)
    if reaction_existed.exists() and reaction_existed[0].reaction == react:
        reaction_existed.delete()
    elif not reaction_existed.exists():
        reaction = Reaction.objects.create(post_id=post, user_id=user, reaction=react)
    else:
        reaction_existed.delete()
        Reaction.objects.create(post_id=post, user_id=user, reaction=react) 
   
    if len(post.reaction_set.filter(reaction = 'dislike')) == 10:
        post.delete()
        return redirect ('homepage')
    return redirect("post", id=id)


# Comment

def add_comment(request,id):
    user = request.user
    post = Post.objects.get(id=id)

    if request.method == "POST":
       comment_content = request.POST.get('comment_content')
       Comment.objects.create(post_id=post, user_id=user, cmnt_content=comment_content)
    
    return redirect('post',id)


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
          
#users    
def list_users(request):
        all_users = User.objects.all()   
        context = { "users" : all_users }
        return render(request, "blogApp/admin.html", context)
    
#category 
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

#unlock
def unlocked(request, id):
    userlock = User.objects.get(id = id)
    userlock.user_status = 'unlocked'
    userlock.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#post crud   


#update post 
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

#update category
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

 #delete post   
def deletepost( request, id ):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('list_post')
    
#category crud

#delete category  
def deletecategory( request, id ):
    category = Category.objects.get(id = id)
    category.delete()
    return redirect('list_categories')
             

