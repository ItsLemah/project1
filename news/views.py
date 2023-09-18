from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
  url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=4f777e3cd76f4c34a020e7d57320ddbf'
  crypto_news = requests.get(url).json()
  a = crypto_news['articles']
  desc =[]
  title =[]
  img =[]
  author =[]
  date =[]
  details =[]
  for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        author.append(f['author'])
        date.append(f['publishedAt'])
        
  mylist = zip(title, desc, img, author, date)
  context = {'mylist': mylist}
  return render(request, 'news.html', context)