from django.shortcuts import render,  get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, PostFormUpdate, CommentForm
from django.urls import reverse_lazy, reverse
import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    # fields = '__all__'
    form_class = CommentForm
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id'] #will make the order be last in first (would be better to use date field)
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_object(self):
        # Use get_object_or_404 to retrieve the Post or raise a 404 if not found
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['comments'] = self.object.comments.all().order_by('-date_added')
        context['total_likes'] = current_post.total_likes()
        context["cat_menu"] = cat_menu
        context['liked'] = liked
        return context

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
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {"category_list": category_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    if not category_posts.exists():  # Se não houver posts com a categoria solicitada
        raise Http404("Uma de duas opções: \n1) Categoria não encontrada \n2) Não há posts nesta categoria")
    return render(request, 'categories.html', {'cats':cats.title(), "category_posts": category_posts})

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
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model=Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    
    
   