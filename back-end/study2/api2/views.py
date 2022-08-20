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

from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView, UpdateAPIView
from blog.models import Comment, Post
from .serializers import CommentSerializer, PostListSerializer, PostRetrieveSerializer, PostLikeSerializer
from rest_framework.response import Response
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class =PostLikeSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {'like' : instance.like +1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(data['like'])