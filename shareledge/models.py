from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    phoneNo = models.CharField(max_length=15)
    job = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    verified = models.BooleanField(null=True)

class Article(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    datePosted = models.CharField(max_length=20, default="")
    timePosted = models.CharField(max_length=20, default="")
    category = models.CharField(max_length=300)
    content = RichTextField(null=True, blank=True, config_name="special", external_plugin_resources=[(
        'youtube', '/static/shareledge/ckeditor-plugins/youtube/youtube/', 'plugin.js',
    )])
    #content = models.CharField(max_length=25000)
    contentImage = models.URLField()
    views = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="on")
    message = models.CharField(max_length=2000)
    datePosted = models.CharField(max_length=20)
    timePosted = models.CharField(max_length=20)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rated_by")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="rate")
    rating = models.IntegerField(default=0)

class userGuidePoint(models.Model):
    title = models.CharField(max_length=1000)
    content = RichTextField()

class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suber")
    email = models.EmailField()