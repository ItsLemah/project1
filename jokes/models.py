from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from ent1.settings import AUTH_USER_MODEL

class Post(models.Model):
    STATUS = (
        (0, "draft"),
        (1, "Published")
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique=True, blank=True)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='jokes_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
        