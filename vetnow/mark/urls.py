from django.urls import path
from . import views

urlpatterns = [
    path('marked/', views.ListMarkedProducts.as_view(), name='marked_products'),
    path('marked/delete/<int:pk>/', views.MarkedProductDelete.as_view(), name='marked_delete'),
    path('marked/added_or_delete/<int:pk>/', views.CreateOrRemoveMarkProduct.as_view(), name='create_mark'),
]