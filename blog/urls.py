from django.contrib import admin
from django.urls import path
from blog.views import index, get_post, get_tags


urlpatterns = [
    path('', index),
    path('post/<int:post_id>', get_post),
    path('tag/<int:id>/', get_tags)
]