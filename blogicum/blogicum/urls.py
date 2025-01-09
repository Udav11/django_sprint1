from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('blog.urls', namespace='homepage')),
    path('admin/', admin.site.urls),
]