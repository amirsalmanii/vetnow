from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/detail/<str:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/update/<str:slug>/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/delete/<str:slug>/', views.NewsDeleteView.as_view(), name='news_delete'),
    path('admin/user/list/', views.AdminUserListView.as_view(), name='admins_list'),
]