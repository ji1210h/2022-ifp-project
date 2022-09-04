from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length = 24,
        min_length = 8,
        write_only =True,
    )
    
    token = serializers.CharField(max_length = 255, read_only = True)