from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'avatar',
        )


class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    parent = serializers.SerializerMethodField(
        read_only=True, method_name='get_chid_comments'
    )

    class Meta:
        model = Comment
        fields = (
            'user',
            'parent',
            'body',
            'approved',
        )

    def get_chid_comments(self, obj):
        """ self referral field """
        serializer = CommentsSerializer(
            instance=obj.comments.all(),
            many=True
        )
        return serializer.data