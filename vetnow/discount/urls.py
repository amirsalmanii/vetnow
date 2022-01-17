from django.urls import path
from . import views

urlpatterns = [
    path('discount_create/', views.DiscountCreateView.as_view(), name='discount_create'),
    path('discount_update/<int:pk>/', views.DiscountUpdateView.as_view(), name='discount_create'),
]