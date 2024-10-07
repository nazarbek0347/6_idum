from django.contrib import admin
from django.urls import path, include
from .views import contact,home,blog,about

urlpatterns = [
    path('',home,name='homePage'),
    path('contact',contact,name='contactPage'),
    path('blog',blog,name='blogPage'),
    path('about',about,name='aboutPage')
]
