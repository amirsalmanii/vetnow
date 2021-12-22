from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('categoies/', views.CategoriesView.as_view(), name='send_categories'),
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('product/<slug:slug>/', views.ProductDetaiView.as_view(), name='product_detail'),
    path('category/<slug:slug>/', views.ProductByCategory.as_view(), name='category_products'),
    path('product/delete/<slug:slug>/', views.ProductDelete.as_view(), name='product_delete'),
]