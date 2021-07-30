from django.db import models
from django.db.models.query import BaseIterable
from django.contrib.auth.models import User
from django.utils import tree

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    image = models.ImageField( upload_to = 'pics', default = 'static/image/fs1.jpg')

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True)
    trending = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text