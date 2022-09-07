from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import get_user_model

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length = 24,
        min_length = 8,
        write_only =True,
    )
    class Meta:
        model = get_user_model()
        fields = ['email','profile_image','username','password','date_of_birth','token']
    
    token = serializers.CharField(max_length = 255, read_only = True)
    
        
    def create(self, User_data):
        return get_user_model().objects.create_user(**User_data)