from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.Contact, name='contact'), 
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('search', views.search, name='search'), 
    path('posts/', views.Post, name='posts'), 
]