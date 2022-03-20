from rest_framework import serializers


class VerifyToCartSerializer(serializers.Serializer):
    tracking_code = serializers.CharField(max_length=16, allow_null=False)