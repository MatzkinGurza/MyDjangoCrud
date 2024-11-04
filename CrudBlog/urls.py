from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView
#from . import views
from django.urls import path

urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    #<int:pk> completes the url with the primary key of the blog entry (assigned on creation)
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='categories'),
    path('category-list/', CategoryListView, name='category_list'),

]
