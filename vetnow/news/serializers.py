from rest_framework import serializers
from .models import News
from accounts.models import User


class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class NewsSerializer(serializers.ModelSerializer):
    author = UserListSerializer()

    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
