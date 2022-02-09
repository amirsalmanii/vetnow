from django.urls import path
from . import views

urlpatterns = [
    path('tokens/', views.TokenList.as_view(), name='list_tokens'),
]