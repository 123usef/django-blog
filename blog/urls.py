from django.urls import path
from . import views
urlpatterns = [
  path('',views.homepage ,name = 'homepage'),
   path('homepage/',views.homepage , name = 'homepage'),
  path('register/',views.register , name = 'register'),
  path('login/',views.userlogin , name = 'login'),
  path('logout/',views.userlogout , name = 'logout')
]

