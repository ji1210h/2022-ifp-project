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

from typing import OrderedDict
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView, GenericAPIView
from blog.models import Category, Comment, Post, Tag
from .serializers import CateTagSerializer, CommentSerializer, PostListSerializer, PostRetrieveSerializer, PostLikeSerializer
from rest_framework.response import Response

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    #serializer_class =PostLikeSerializer
    #PACTH method
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     data = {'like' : instance.like +1}
    #     serializer = self.get_serializer(instance, data=data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #     return Response(data['like'])
    
    #GET method
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)
    
class CateTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data={
            'catelist': cateList,
            'taglist': tagList,
        }
        
        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)
    
class PostNumberPagination(PageNumberPagination):
    page_size = 3
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('PostList', data),
            ('PageCnt', self.page.paginator.num_pages),
            ('curPage', self.page.number),
        ]))
    
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostNumberPagination
    
    def get_serializer_context(self):
        return {
            'request' : None,
            'format' : self.format_kwarg,
            'view' : self
        }