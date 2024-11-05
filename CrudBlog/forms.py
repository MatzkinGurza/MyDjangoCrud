from django import forms
from .models import Post, Category, Comment

choices = [x for x in Category.objects.all().values_list('name','name')] #to pass choices into forms select
class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Post
        fields = ('title', 
                  'tag', 
                  'author', 
                  'category',
                  'body' )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'authorID', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'})
        }

class PostFormUpdate(forms.ModelForm):
    image = forms.ImageField(required=False)  # campo para upload de imagem

    class Meta: 
        model = Post
        fields = ('title', 
                  'tag',  
                  'body',
                   'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'write your title here'}), 
            'tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'choose a tag for the post'}), 
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'write your post here'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
   
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'Comment_authorID', 'type': 'hidden'}), 
        'body': forms.Textarea(attrs={'class': 'form-control'}), 
        }