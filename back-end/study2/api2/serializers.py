from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import get_category_model, get_post_model, get_comment_model, get_tag_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="Category.name")
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
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_category_model()
        fields = ['name']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_tag_model()
        fields = ['name']
        
# class CateTagSerializer(serializers.Serializer):
#     catelist = CategorySerializer(many=True)
#     taglist = TagSerializer(many=True)

class CateTagSerializer(serializers.Serializer):
    catelist = serializers.ListField(child=serializers.CharField())
    taglist = serializers.ListField(child=serializers.CharField())