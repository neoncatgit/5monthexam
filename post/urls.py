from django.contrib import admin
from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    )

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:id>/', PostDetailAPIView.as_view()),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view()),
]