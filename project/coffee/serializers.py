from asyncore import read
from email.policy import default
from hashlib import scrypt
from unittest.util import _MAX_LENGTH
from urllib import request
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True, default= "profile/2022/10/default.png")
    password = serializers.CharField(
        max_length = 24,
        min_length = 8,
        write_only =True,
    )
    class Meta:
        model = User
        fields = [
            'email',
            'profile_image',
            'username',
            'password',
            'date_of_birth',
            'token'
            ]
    
    token = serializers.CharField(max_length = 255, read_only = True)
    
        
    def create(self, User_data):
        return User.objects.create_user(**User_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    # username = serializers.CharField(max_length=255, read_only=True) #로그인에서 사용하지 않지만 값은 반환 해야 되기에 #read_only
    password = serializers.CharField(max_length=24, write_only=True) #보안상의 문제로 반환하면 안 되기에 write_only
    last_login = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None:
            raise serializers.ValidationError(
                "e-mail을 입력해주세요."
            )
        if password is None:
            raise serializers.ValidationError(
                "비밀번호를 입력해주세요."
            )
        
        user = authenticate(email=email, password=password)
        
        if user is None:
            raise serializers.ValidationError(
                "e-mail 혹은 비밀번호를 제대로 입력했는 지 확인해주세요."
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                "이 사용자는 비활성화 상태입니다."
            )
        
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        
        
        return{
            'token' : user.token
        }
        
class UserReadSerializer(serializers.ModelSerializer):
    post_set = serializers.SlugRelatedField(many=True, slug_field='title', read_only=True)
    Post = serializers.SlugRelatedField(many=True, slug_field='title', read_only=True)
    profile_image = serializers.ImageField(use_url=True)
    class Meta:
        model = User
        fields = [
            'profile_image',
            'username',
            'date_of_birth',
            'post_set',
            'Post'
            ]

class UserUpdateSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True,default = "profile/2022/10/default.png")
    password = serializers.CharField( max_length = 24, min_length = 8)
    post_set = serializers.SlugRelatedField(many=True, slug_field='title', read_only=True)
    Post = serializers.SlugRelatedField(many=True, slug_field='title', read_only=True)
    class Meta:
        model = User
        fields = [
            'profile_image',
            'email',
            'username',
            'password',
            'date_of_birth',
            'post_set',
            'Post'
        ]
        
        read_only_fields = ('email', 'date_of_birth', 'post_set', 'Post')
        
    def update( self, instance, validated_data):
        
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
            
        if password is not None:
            instance.set_password(password)
    
        instance.save()
        
        return instance
    
class PostListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    bookmark_user = serializers.IntegerField(source="bookmark_user.count", read_only=True)
    class Meta:
        model = Post
        fields = [
            'image',
            'title',
            'bookmark_user',
            'category']

class PostReadSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    material = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    bookmark_user = serializers.IntegerField(source="bookmark_user.count", read_only=True)
    class Meta:
        model = Post
        fields =[
            
            'category',
            'title',
            'material',
            'content',
            'create_dt',
            'bookmark_user',
            'user'
        ]

class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, default= "coffee/2022/10/default.jpg")
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'material',
            'image',
            'content',
            'user',
        ]
class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    material = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Material.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = [
            'image',
            'category',
            'title',
            'material',
            'content',
            'update_dt',
            'user',
        ]

class PostBookmarkSerializer(serializers.ModelSerializer):
    Bookmark_user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Post
        fields = ["bookmark_user"]