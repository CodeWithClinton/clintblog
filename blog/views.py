from django.shortcuts import render
from . models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    trending = Post.objects.filter(trending = True)
    posts = Post.objects.filter(trending = False)
    return render(request, 'blog/index.html', {"trending": trending, "posts": posts})

def readmore(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comment_set.all()
    newComment = None
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.post = post
            newComment.save()
            return HttpResponseRedirect(reverse('readmore', kwargs={'slug': slug}))
    return render(request, 'blog/readmore.html', {"post":post, "comments": comments, "form":form, "newComment": newComment})