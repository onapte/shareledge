from django.urls import path
from . import views

app_name = 'shareledge'

urlpatterns = [
    path('', views.home, name="homePage"),
    path('create', views.create, name="createPage"),
    path('articles', views.allArticles, name="allArticles"),
    path('logout', views.logout_view, name="logout"),
    path('articles/<int:articleId>', views.article, name="article"),
    path('user-guide', views.userGuide, name="userGuide"),
    path('articles/edit/<int:articleId>', views.editArticle, name="edit"),
    path('login', views.login_view, name="login"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('register', views.register, name="register"),
    path("articles/comment/<int:articleId>", views.comment, name="comment"),
    path('<int:userId>/profile', views.userProfile, name="profile")
]