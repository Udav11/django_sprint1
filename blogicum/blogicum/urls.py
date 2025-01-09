from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('blog.urls', namespace='homepage')),
    path('posts/<int:id>/', include('blog.urls', namespace='homepage1')),
    path('category/<slug:category_slug>/', include('blog.urls', namespace='homepage2')),
    path('pages/', include('pages.urls', namespace='pages')),
]