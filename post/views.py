from django.shortcuts import render
from .models import Post

from .forms import PostForm


def home(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'post/home.html', context)

def post_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'post/detail.html', context)
