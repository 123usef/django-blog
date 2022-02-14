from django.urls import path
from . import views
urlpatterns = [
  path('',views.base ,name = 'base'),
  path('home/',views.home , name = 'home'),
  path('homepage/',views.homepage , name = 'homepage'),
  path('register/',views.register , name = 'register'),
  path('login/',views.userlogin , name = 'login'),
  path('profile/',views.profile , name = 'profile'),
  path('post/',views.post , name = 'post'),
  path('useradmin/',views.useradmin , name = 'useradmin'),
  path('logout/',views.userlogout , name = 'logout')
]

