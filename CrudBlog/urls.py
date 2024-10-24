from .views import HomeView, ArticleDetailView
#from . import views
from django.urls import path

urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    #<int:pk> completes the url with the primary key of the blog entry (assigned on creation)

]
