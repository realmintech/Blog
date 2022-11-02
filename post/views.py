from django.shortcuts import render, redirect
from .models import Post

from .forms import PostForm


def home(request, *args, **kwargs):
    post = Post.objects.all()
    context = {"post": post}
    return render(request, 'post/home.html', context)

def post_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'post/detail.html', context)

def user_post(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        user = form.save()
        user.creator =  request.user
        user.save()
        return redirect("home")


    return render(request, 'post/user_post.html', context)