
from django.contrib import admin
from django.urls import path
from .views import register,loginUser
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',loginUser,name='loginUser')
]
