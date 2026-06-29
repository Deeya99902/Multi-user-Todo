
from django.contrib import admin
from django.urls import path
from todo.views import home,login,signup



urlpatterns = [
    path('', home),
     path('login', login),
      path('signup', signup),
]
