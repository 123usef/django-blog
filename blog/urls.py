from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
  
  path('homepage/',views.homepage , name = 'homepage'),
  path('register/',views.register , name = 'register'),
  path('login/',views.userlogin , name = 'login'),
  path('logout/',views.userlogout , name = 'logout'),
  # categories
  path('det_category/<int:id>',views.det_category, name='det_category'),
  path('subscribe/<int:id>',views.subscribe, name='subscribe'),
  path('user_subscriptions',views.user_subscriptions, name='user_subscriptions')
]

