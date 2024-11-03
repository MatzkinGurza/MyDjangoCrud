from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255, default="Unspecified")
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))

class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, default="Unspecified") #parameter: default="default tag" should be used if creating this field after already having other inputs
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)  # Campo para o link da imagem
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
    
    

        