from django.urls import path 
from . import views
urlpatterns = [
   path('',views.navbar ,name = 'nav'),
   path('home/',views.home , name = 'home'),
   path('login/',views.login,name = 'login'),
   path('signup/',views.signup,name = 'signup')

]
