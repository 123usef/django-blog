from django.urls import path
from . import views
urlpatterns = [
  path('',views.navbar ,name = 'nav'),
  path('home/',views.home , name = 'home'),
  path('register/',views.register , name = 'register'),
  path('login/',views.userlogin , name = 'login'),
  path('logout/',views.userlogout , name = 'logout')
]

