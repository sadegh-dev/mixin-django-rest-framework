from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-release_datetime')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)      
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request, 'add-post.html', context)

