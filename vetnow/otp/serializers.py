from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TokenListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'
