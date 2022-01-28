from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from . import serializers
from .models import News


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsCreateView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    permission_classes = (IsAdminUser,)


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    lookup_field = 'slug'


class NewsUpdateView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUser,)


class NewsDeleteView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUser,)
