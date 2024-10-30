from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, PostFormUpdate
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id'] #will make the order be last in first (would be better to use date field)

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'tag','body')

class UpdatePostView(UpdateView):
    model=Post
    form_class = PostFormUpdate
    template_name= 'update_post.html'

class DeletePostView(DeleteView):
    model=Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')
   