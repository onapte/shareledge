from django.contrib import admin
from .models import Article, User, Comment, Rating, userGuidePoint, Subscriber

# Register your models here.
admin.site.register(Article)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(userGuidePoint)
admin.site.register(Subscriber)
