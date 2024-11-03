from django.shortcuts import render,  get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, PostFormUpdate
from django.urls import reverse_lazy
import requests
from django.conf import settings


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id'] #will make the order be last in first (would be better to use date field)
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_object(self):
        # Use get_object_or_404 to retrieve the Post or raise a 404 if not found
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'tag','body')

    def form_valid(self, form):
        image_file = form.cleaned_data.get('image')
        if image_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                form.instance.image_url = data['data']['link']

        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model=Post
    form_class = PostFormUpdate
    template_name= 'update_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        image_file = form.cleaned_data.get('image')
        if image_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                form.instance.image_url = data['data']['link']
        
        return super().form_valid(form)

class DeletePostView(DeleteView):
    model=Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')
   