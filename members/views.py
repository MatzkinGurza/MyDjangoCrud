from django.shortcuts import render,  get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PostProfilePageForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
import requests
from django.conf import settings
from CrudBlog.models import Profile, Post

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    #fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        image_file = form.cleaned_data.get('image')
        if image_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                form.instance.profilepic_url = data['data']['link']
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    form_class = PostProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio', 'profilepic_url', 'website_url', 'contact']
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
                form.instance.profilepic_url = data['data']['link']

        return super().form_valid(form)

       
        

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        user_posts = Post.objects.filter(author=page_user.user)
        context["user_posts"] = user_posts
        return context
    

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    forms_classe = PasswordChangeForm
    success_url = reverse_lazy('home')