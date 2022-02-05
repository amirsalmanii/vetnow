from django.urls import path
from . import views

urlpatterns = [
    path('marked/', views.ListMarkedProducts.as_view(), name='marked_products'),
    path('marked/delete/<int:pk>/', views.MarkedProductDelete.as_view(), name='marked_delete'),
]