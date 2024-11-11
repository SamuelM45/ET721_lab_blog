from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost


def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')


def post_edit(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', id=post.id)
    return render(request, 'blog/post_form.html', {'post': post})
