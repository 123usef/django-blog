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