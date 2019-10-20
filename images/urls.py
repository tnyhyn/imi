from django.urls import path
from .models import Post

from . import views


urlpatterns = [
    path('/', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('myimages/<int:pk>/', views.delete_file, name='delete_file'),
    path('register/', views.register, name='register'),
    path('myimages/', views.myimages, name='myimages'),
]


