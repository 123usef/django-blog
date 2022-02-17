from blog.models import Category
# from django.contrib.auth.decorators import login_required

def navbarfun(request):
    cats = Category.objects.all()
    if request.user.is_anonymous:
        return { "cats": cats}
    else :
        user = request.user
        subs = user.subscriptions_set.all()
        subs_id = []
        for sub in subs:
            subs_id.append(sub.cat_id)
        return { "cats": cats, "subs_id": subs_id}