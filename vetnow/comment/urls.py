from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('comments/<slug:slug>/', views.CommentsView.as_view(), name='comments'),
]