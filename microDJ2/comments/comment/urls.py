from django.urls import path
from .views import CommentView, CommentByPost

urlpatterns = [
    path('posts/<str:pk>/comments', CommentByPost.as_view()),
    path('comments/',CommentView.as_view())
]
