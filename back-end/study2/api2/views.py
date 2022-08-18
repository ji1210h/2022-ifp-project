# from rest_framework import viewsets
# from django.contrib.auth.models import User

# from api2.serializers import UserSerializer, PostSerializer, CommentSerializer
# from blog.models import get_post_model, get_comment_model

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = get_post_model().objects.all()
#     serializer_class = PostSerializer
    
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = get_comment_model().objects.all()
#     serializer_class = CommentSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from blog.models import Comment, Post
from .serializers import CommentSerializer, PostListSerializer, PostRetrieveSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer