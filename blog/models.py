from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=30)
    def __str__(self):
        return self.cat_name

class Subscriptions(models.Model):
    cat_id = models.ForeignKey(Category)



