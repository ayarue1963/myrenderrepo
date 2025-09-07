from django.urls import path
from .views import create_post
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contactus/', views.contactus, name='contactus'),
]

