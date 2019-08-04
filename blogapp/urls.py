from django.contrib import admin
from django.urls import path, include
import blogapp.views

urlpattern = [
    path('<int:blog_id>', blogapp.views.detail, name="detail"), 
    path('new/',blogapp.views.new, name="new"),
    path('create/', blogapp.views.create, name="create"),
    path('mypage/', blogapp.views.mypage, name="mypage"),
]