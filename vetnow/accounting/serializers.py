from rest_framework import serializers


class DateSerilizer(serializers.Serializer):
    slug = serializers.CharField(max_length=200, allow_null=False, allow_blank=False)
    date_start = serializers.CharField(max_length=200, allow_null=False, allow_blank=False)
    date_end = serializers.CharField(max_length=200, allow_null=False, allow_blank=False)