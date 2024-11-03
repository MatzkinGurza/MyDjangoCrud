from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('article/<int:pk>', views.article_detail, name="article-detail"),
    path('add_post/', views.add_post, name='add_post'),
    path('article/edit/<int:pk>', views.update_post, name='update_post'),
    path('article/<int:pk>/delete', views.delete_post, name='delete_post'),
]

