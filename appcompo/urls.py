"""composition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .apiviews import *


router = DefaultRouter()
router.register('categoriea', CategorieViewSet, basename="categorie")
router.register('auteur', AuteurViewSet,basename="auteur")
router.register('article', ArticleViewSet, basename="article")
router.register('comment', CommentaireViewSet,basename="comment")
router.register('tag', TagViewSet,basename="tag")


urlpatterns = [
    path('', views.index , name="home"),
    path('fashion/', views.fashion , name="fashion"),
    path('about/', views.about , name="about"),
    path('travel/', views.travel , name="travel"),
    path('single/', views.single , name="single"),
    path('contact/', views.contact , name="contact"),
]
urlpatterns += router.urls