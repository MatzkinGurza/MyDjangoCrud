from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="home"),
    path('article/<int:pk>/', views.post_detail, name="article-detail"),
    path('add_post/', views.post_create, name='add_post'),
    path('article/edit/<int:pk>/', views.post_update, name='update_post'),
    path('article/<int:pk>/delete/', views.post_delete, name='delete_post'),
]

