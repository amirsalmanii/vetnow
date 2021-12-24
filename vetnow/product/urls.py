from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('categoies/', views.CategoriesView.as_view(), name='send_categories'),
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('product/<str:slug>/', views.ProductDetaiView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.ProductByCategory.as_view(), name='category_products'),
    path('product/delete/<str:slug>/', views.ProductDelete.as_view(), name='product_delete'),
]