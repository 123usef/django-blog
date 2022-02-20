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
  path('pagination/',views.pagination , name = 'pagination'),

  
  # categories
  path('det_category/<int:id>',views.det_category, name='det_category'),
  path('subscribe/<int:id>',views.subscribe, name='subscribe'),
  path('user_subscriptions',views.user_subscriptions, name='user_subscriptions'),
  path('unsubscribe/<int:id>',views.unsubscribe, name='unsubscribe'),
  
  # Posts
   path('post/<int:id>',views.det_post, name='post'),
   path('Apipost/<int:id>',views.Apidet_post, name='Apipost'),
   path('react/<int:id>/<str:react>' , views.add_reaction , name='add_reaction'),
   path('createpost/',views.create_post, name='create_post'),
   
  #  Comment
   path('comment/<int:id>' , views.add_comment , name='add_comment'),

 #admin list all
  path('useradmin/',views.useradmin , name = 'useradmin'),
  path('list_post/',views.list_post , name = 'list_post'),
  path('list_users/',views.list_users , name = 'list_users'),
  path('list_categories/',views.list_categories , name = 'list_categories'),
  path('list_forbidden_word/',views.list_forbidden_word , name = 'list_forbidden_word'),


#admin locked user
  path('locked/<int:id>',views.locked, name='locked'),
  path('unlocked/<int:id>',views.unlocked, name='unlocked'),
  
# admin crud post
  path('deletepost/<int:id>',views.deletepost, name='deletepost'),
  path('updatepost/<int:id>',views.updatepost, name='updatepost'),
  # admin crud category
  path('deletecategory/<int:id>',views.deletecategory, name='deletecategory'),
  path('updatecategory/<int:id>',views.updatecategory, name='updatecategory'),
  path('addcategory',views.addcategory, name='addcategory'),
  
  # admin crud forbidden word
  path('del_forbidden_word/<int:id>',views.del_forbidden_word, name='del_forbidden_word'),
  path('updateforbidden_word/<int:id>',views.updateforbidden_word, name='updateforbidden_word'),
  path('addforbidden_word',views.addforbidden_word, name='addforbidden_word'),







  
   
]

