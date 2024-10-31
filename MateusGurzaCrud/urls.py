from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('CrudBlog.urls')),
    path('members/', include('django.contrib.auth.urls')), #this includes the login url directly to the blog
    path('members/', include('members.urls')),

]
