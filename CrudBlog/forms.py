from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Post
        fields = ('title', 
                  'tag', 
                  'author', 
                  'body' )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'author': forms.Select(attrs={'class': 'form-control'}), 
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'})
        }

class PostFormUpdate(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Post
        fields = ('title', 
                  'tag',  
                  'body' )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'})
        }