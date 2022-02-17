from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from . import serializers
from .models import News
from accounts.serializers import UserListSerializer
from accounts.views import MyPagination

User = get_user_model()


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = MyPagination


class LastThreeNewsListView(APIView):
    def get(self, request):
        queryset = News.objects.all()[:3]
        serializer = serializers.NewsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=200)


class NewsCreateView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    permission_classes = (IsAdminUser,)
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


class AdminUserListView(ListAPIView):
    queryset = User.objects.filter(is_admin=True)
    serializer_class = UserListSerializer
