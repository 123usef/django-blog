from unicodedata import name
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
  path('logout/',views.userlogout , name = 'logout'),
  path('search/',views.search , name = 'search'),
  # categories
  path('det_category/<int:id>',views.det_category, name='det_category'),
  path('subscribe/<int:id>',views.subscribe, name='subscribe'),
  path('user_subscriptions',views.user_subscriptions, name='user_subscriptions'),
  path('unsubscribe/<int:id>',views.unsubscribe, name='unsubscribe'),
  # Posts
   path('post/<int:id>',views.det_post, name='post'),
   path('react/<int:id>/<str:react>' , views.add_reaction , name='add_reaction')
]

