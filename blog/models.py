from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):

    statuses = (("locked", "locked"), ("unlocked", "unlocked"))
    roles = (("user", "user"), ("admin", "admin"))
    user_status = models.CharField(max_length=20, choices=statuses, default="unlocked")
    user_role = models.CharField(max_length=20, choices=roles, default="user")

    def __str__(self):
        return self.username

# creating category table
class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name


# creating subscription table
class Subscriptions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cat_id)


# create post table
class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_picture = models.ImageField(null=True, blank=True , upload_to="img/" ,default='img/Default_Image.png')
    post_content = models.CharField(max_length=5000)
    post_cr_date = models.DateTimeField(auto_now_add=True)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title


class Tags(models.Model):
    tag_name = models.CharField(max_length=30)
    # post id pending upon making posts table
    # post id updated
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


# create comment.s
class Comment(models.Model):
    cmnt_cr_date = models.DateTimeField(auto_now_add=True)
    cmnt_content = models.CharField(max_length=200, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)  # fk-post
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # fk-user
#    comment reply
    # parent = models.ForeignKey('self', null=True, related_name='replies')
    # def __str__(self):
    #     return self.text

# create reactions.s
class Reaction(models.Model):

    roles = (("like", "like"), ("dislike", "dislike"))
    reaction = models.CharField(max_length=8, choices=roles)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)  # fk-post
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # fk-user
        
class ForbiddenWords(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
