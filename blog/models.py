from django.db import models

# Create your models here.

#comment 

class Comment(models.Models):
    cmnt_cr_date = models.DateTimeField(auto_now_add=True)
    cmnt_content = models.CharField(max_length=200, null=True)
   
   # def __str__(self):
      #return self.comment  

#reactions
class Reaction(models.Models):

    roles = (
        ('like' , 'like'),
        ('dislike' , 'dislike')
     )
    reaction = models.charField(choices=roles)
    
    #def __str__(self):
      #return self.reaction
class User(models.Model):
    statuses = (
        ( 'locked' , 'locked'),
        ( 'unlocked' , 'unlocked')
    )
    roles = (
        ( 'user' , 'user'),
        ( 'admin' , 'admin')
           )
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=40)
    user_password = models.CharField(max_length=30)
    user_cr_date = models.DateTimeField(auto_now_add=True)
    user_status = models.CharField(max_length=20 , choices=statuses)
    user_role = models.CharField(max_length=20 , choices=roles)
    def __str__(self) :
        return self.user_name
    
class Category(models.Model):
    cat_name = models.CharField(max_length=30)
    def __str__(self):
        return self.cat_name

class Subscriptions(models.Model):
    user_id = models.ForeignKey(User)
    cat_id = models.ForeignKey(Category)
    



