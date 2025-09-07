from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
#from django.db.models import Q
#from django.contrib.auth.models import User

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_posts.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    #return render(request, 'posts/home.html', {'posts': posts})
    return render(request, 'posts/post_list.html', {'posts': posts})

def dashboard(request): 
    posts = Post.objects.all() 
    return render(request, 'posts/dashboard.html', {'posts': posts})

def home(request): 
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def contactus(request): 
    return render(request, 'posts/contactus.html')