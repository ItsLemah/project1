from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

def search(request):
  if request.method == "POST":
    searched = request.POST['searched']
    return render(request, 'search.html', {'searched':searched})
  else:
    return render(request, 'search.html', {})
    
    
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
def post(request):
  #post = Post.objects.all()
 # queryset = Post.objects.get.filter(status=1).order_by('-created_on')
  author = Post.objects.get('author')
  title = Post.objects.get('title')
  content = Post.objects.get('content')
  created_on = Post.objects.get('created_on')
  
  all_cont = (author, title, content, created_on)
  
  context = {
   # 'post':post, 
   # 'queryset':queryset, 
    'all_cont':all_cont, 
  }
  return render(request, 'posts.html', context)
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def Contact(request):
  return render(request, 'contact.html')