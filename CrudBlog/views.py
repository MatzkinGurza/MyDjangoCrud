from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.conf import settings
import requests

def post_list(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article_details.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        tag = request.POST.get("tag")
        body = request.POST.get("body")
        image = request.FILES.get("image")

        image_url = None
        if image:
            # Upload image to Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()
            if response.status_code == 200 and data['success']:
                image_url = data['data']['link']

        # Save the post
        post = Post.objects.create(
            title=title,
            tag=tag,
            author=request.user,
            body=body,
            image_url=image_url,
        )
        return redirect('home')
    return render(request, 'add_post.html')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.tag = request.POST.get('tag')
        post.body = request.POST.get('body')
        image = request.FILES.get("image")
        if image:
            # Upload image to Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()
            if response.status_code == 200 and data['success']:
                post.image_url = data['data']['link']
        
        post.save()
        return redirect('article-detail', pk=post.pk)
    return render(request, 'update_post.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})

