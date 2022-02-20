from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subscriptions)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(ForbiddenWords)



