from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, PostFormUpdate
from django.urls import reverse_lazy
import requests
from django.conf import settings

# def home(request):
#     return render(request, 'home.html', {})

def home(request):
        posts = Post.objects.all().order_by('-post_date')
        return render(request, 'home.html', {'posts': posts})

def article_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article_details.html', {'post': post})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle image upload to Imgur
            image_file = form.cleaned_data.get('image')
            if image_file:
                # Upload the image to Imgur
                url = "https://api.imgur.com/3/image"
                headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
                files = {'image': image_file.read()}

                response = requests.post(url, headers=headers, files=files)
                data = response.json()

                if response.status_code == 200 and data['success']:
                    # Set the `image_url` field in the post instance
                    post = form.save(commit=False)  # Save form data without committing to DB
                    post.image_url = data['data']['link']
                    post.save()  # Now save with `image_url` populated
                    return redirect('home')

            # If no image, simply save the form data
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostFormUpdate(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Handle image upload to Imgur if a new image is provided
            image_file = form.cleaned_data.get('image')
            if image_file:
                # Upload the image to Imgur
                url = "https://api.imgur.com/3/image"
                headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
                files = {'image': image_file.read()}

                response = requests.post(url, headers=headers, files=files)
                data = response.json()

                if response.status_code == 200 and data['success']:
                    # Update the `image_url` field in the post instance
                    post.image_url = data['data']['link']

            # Save the form with updated data
            form.save()
            return redirect('article-detail', pk=post.pk)
    else:
        form = PostFormUpdate(instance=post)
    
    return render(request, 'update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})