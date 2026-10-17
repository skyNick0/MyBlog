from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_posts(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Post.objects.all().filter(author=author)

    return render(request, 'blog/author_posts.html', {
        'author': author,
        'posts': posts
    })