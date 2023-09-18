from . import views
from django.urls import path 

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('jokes/', views.PostListView.as_view(), name='post_list'),
]
