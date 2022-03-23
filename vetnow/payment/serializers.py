from rest_framework import serializers


class VerifyToCartSerializer(serializers.Serializer):
    tracking_code = serializers.CharField(max_length=16, allow_null=False)


class TotalPriceSerializer(serializers.Serializer):
    total_price = serializers.IntegerField(allow_null=False)

