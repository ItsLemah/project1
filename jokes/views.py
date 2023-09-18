from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from .models import Post 

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-publish')
    context_object_name = 'posts'
    paginate_by = 20
    template_name = 'list.html'
