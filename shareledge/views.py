from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.forms import widgets
from django.shortcuts import render
from django.urls.base import translate_url
from django.views.generic import View
from .models import Article, User, Comment, Rating, userGuidePoint, Subscriber
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from datetime import datetime, date
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core.mail import send_mail
from capstone.settings import EMAIL_HOST_USER
from io import BytesIO
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.conf import settings
import os
from django.db import IntegrityError
from django.shortcuts import redirect
from django.utils.safestring import SafeString
from django import forms
from ckeditor.fields import RichTextField, RichTextFormField
import json
from django.db.models import Q
from django.utils.html import strip_tags

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'contentImage']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'category': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
            'content': RichTextFormField(config_name="default"),
            'contentImage': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Image'})
        }

# Create your views here.
def home(request):
    return render(request, 'shareledge/home.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("shareledge:homePage"))
        else:
            return render(request, "shareledge/login.html", {
                "message": "Invalid username and/or password.",
                
            })
    else:
        return render(request, "shareledge/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('shareledge:homePage'))

def create(request):
    articles = Article.objects.all()
    if request.user.is_authenticated == False or request.user.verified == False:
        return render(request, 'shareledge/unauthorized.html')
    if request.method == "POST":
        title = request.POST['title']
        category = request.POST['category']
        user = request.user
        content = request.POST['content']
        contentImage = request.POST['contentImage']
        datePosted = date.today().strftime("%B %d, %Y")
        timePosted = datetime.now().strftime('%H:%M')
        newArticle = Article.objects.create(
            title = title,
            category = category,
            content = content,
            user = user,
            contentImage = contentImage,
            datePosted = datePosted,
            timePosted = timePosted
        )
        newArticle.save()
        recipients = Subscriber.objects.all()
        recipientEmails = [recipient.email for recipient in recipients]
        subject = "New article"
        message = f"Hey Shareledger! A user {user} just published a new article. Check it out at! \n \n \n Regards,\n The ShareLEDGE Team"
        send_mail(subject, message, EMAIL_HOST_USER, recipientEmails, fail_silently=False)
        return HttpResponseRedirect(reverse('shareledge:allArticles'))
    form = ArticleForm()
    return render(request, 'shareledge/create.html', {
        'articles': articles,
        'myform': form,
        "toEdit": False
    })

def allArticles(request):
    if request.method == "GET" and "search" in request.GET:
        searchQuery = request.GET['search-query']
        # results = []
        # for article in Article.objects.all():
        #     if searchQuery in article.category:
        #         results += article.category
        results = Article.objects.filter(Q(category__icontains=searchQuery))
        display_info = f"No articles related to '{searchQuery}' found!"
        if results:
            display_info = f"Search results based on '{searchQuery}'"
        return render(request, 'shareledge/articles.html', {
            'articles': results,
            'display_info': display_info
        })
    articles = Article.objects.all()
    for article in articles:
        avg = 0
        for obj in Rating.objects.filter(article = article):
            avg += obj.rating
        if Rating.objects.filter(article = article).count() > 0:
            avg = avg / Rating.objects.filter(article = article).count()
        article.rating = avg
        article.save()

    return render(request, 'shareledge/articles.html', {
        'articles': Article.objects.all().order_by('-rating')
    })

def article(request, articleId):
    article_obj = Article.objects.get(id=articleId)
    article_obj.views += 1
    article_obj.save()
    if request.method == 'POST':
        rating = 0
        if 's1' in request.POST:
            rating = 1
        elif 's2' in request.POST:
            rating = 2
        elif 's3' in request.POST:
            rating = 3
        elif 's4' in request.POST:
            rating = 4
        elif 's5' in request.POST:
            rating = 5
        newRating = Rating.objects.create(
            user = request.user,
            article = article_obj,
            rating = rating
        )
        newRating.save()
    reqUserRated = False
    try:
        if request.user.is_authenticated:
            Rating.objects.get(
                user = request.user,
                article = article_obj
            )
            reqUserRated = True
    except Rating.DoesNotExist:
        reqUserRated = False
    avg = 0
    if article_obj.rate.count() > 0:
        r5 = (Rating.objects.filter(rating=5, article=article_obj).count() / article_obj.rate.count()) * 100
        r4 = (Rating.objects.filter(rating=4, article=article_obj).count() / article_obj.rate.count()) * 100
        r3 = (Rating.objects.filter(rating=3, article=article_obj).count() / article_obj.rate.count()) * 100
        r2 = (Rating.objects.filter(rating=2, article=article_obj).count() / article_obj.rate.count()) * 100
        r1 = (Rating.objects.filter(rating=1, article=article_obj).count() / article_obj.rate.count()) * 100
        for obj in Rating.objects.filter(article = article_obj):
            avg += obj.rating
        avg = avg / Rating.objects.filter(article = article_obj).count()
    else:
        r5 = 0
        r4 = 0
        r3 = 0
        r2 = 0
        r1 = 0
    return render(request, 'shareledge/article.html', {
        'article': article_obj,
        'comments': Comment.objects.filter(article=article_obj),
        'comment_count': Comment.objects.filter(article=article_obj).count(),
        'more_articles': Article.objects.filter(category=article_obj.category).order_by('-rating')[:3],
        'ratings': Rating.objects.filter(article=article_obj),
        'rated': reqUserRated,
        'r5':r5,
        'r4':r4,
        'r3':r3,
        'r2':r2,
        'r1':r1,
        'avg': avg
            })

def userGuide(request):
    points = userGuidePoint.objects.all()
    return render(request, 'shareledge/userGuide.html', {
        'points': points
    })

def editArticle(request, articleId):
    article_obj = Article.objects.get(id = articleId)
    if request.user.is_authenticated == False or article_obj.user != request.user:
        return render(request, 'shareledge/unauthorized.html')
    form = ArticleForm()
    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        
        title = request.POST['title']
        category = request.POST['category']
        content = request.POST['content']
        contentImage = request.POST['contentImage']
        article_obj.title = title
        article_obj.category = category
        article_obj.content = content
        article_obj.contentImage = contentImage
        article_obj.save()
        return HttpResponseRedirect(reverse('shareledge:article', kwargs={'articleId':articleId}))
    
    form = ArticleForm(initial={
        'title': article_obj.title,
        'content': article_obj.content,
        'category': article_obj.category,
        'contentImage': article_obj.contentImage
    })
    return render(request, 'shareledge/create.html', {
        "article_obj": article_obj,
        "myform": form,
        "toEdit": True
    })

def subscribe(request):
    if request.method == "POST":
        recipient = request.POST['email']
        newSuber = Subscriber.objects.create(user = request.user, email = recipient)
        newSuber.save()
        subject = "Thanks for subscribing at ShareLEDGE"
        #message = "Be prepared for receiving django shock!"
        message = render_to_string('shareledge/email.html', {
            'suber': request.user.username
        })
        message = strip_tags(message)
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        return HttpResponseRedirect(reverse('shareledge:allArticles'))

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST["email"]
        phoneNo = request.POST['phone-no']
        job = request.POST['job']
        company = request.POST['company']
        verified = False
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "shareledge/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name, 
                email = email, 
                password = password, 
                phoneNo = phoneNo, 
                job = job, 
                company = company,
                verified = verified
                )
            user.save()
        except IntegrityError:
            return render(request, "shareledge/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return redirect("shareledge:homePage")
    else:
        return render(request, "shareledge/register.html")

@csrf_exempt
def comment(request, articleId):
    if request.user.is_authenticated == False:
        return render(request, 'shareledge/unauthorized.html')
    if request.method == "POST":
        articleObject = Article.objects.get(id = articleId)
        data_dict = json.loads(request.POST.get('dataJson'))
        newComment = Comment.objects.create(
            user = request.user,
            article = articleObject,
            message = data_dict['content'],
            datePosted = date.today().strftime("%B %d, %Y"),
            timePosted = datetime.now().strftime('%H:%M'),
        )
        newComment.save()
        return HttpResponse("success")

def userProfile(request, userId):
    user = User.objects.get(id = userId)
    userArticles = Article.objects.filter(user = user).order_by('-rating')
    return render(request, "shareledge/userProfile.html", {
        'theUser': user,
        'userArticles': userArticles
    })