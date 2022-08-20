from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import get_post_model, get_comment_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_post_model()
        fields = ['id', 'title', 'image', 'like', 'category']

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_post_model()
        exclude = ['create_dt']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_comment_model()
        fields = '__all__'
        
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_post_model()
        fields = ['like']