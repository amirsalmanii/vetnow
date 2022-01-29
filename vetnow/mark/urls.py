from django.urls import path
from . import views

urlpatterns = [
    path('marked/', views.ListMarkedProducts.as_view(), name='marked_products'),
]