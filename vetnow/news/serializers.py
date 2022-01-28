from rest_framework import serializers
from .models import News
from accounts.serializers import UserListSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = UserListSerializer()

    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
