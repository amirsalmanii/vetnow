from django.urls import path
from . import views

urlpatterns = [
    path('discount/list/', views.DiscountListView.as_view(), name='discount_list'),
    path('discount/create/', views.DiscountCreateView.as_view(), name='discount_create'),
    path('discount_update/<int:pk>/', views.DiscountUpdateView.as_view(), name='discount_update'),
    path('discount_detail/<int:pk>/', views.DiscountDetailView.as_view(), name='discount_detail'),
    path('discount_delete/<int:pk>/', views.DiscountDeletView.as_view(), name='discount_delete'),
]