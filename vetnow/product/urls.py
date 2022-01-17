from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('pagination/categories/', views.CategoriesWithPaginationView.as_view(), name='send_categories_with_pagination'),
    path('categories/', views.CategoriesListView.as_view(), name='send_categories'),
    path('category/create/', views.CreateCategory.as_view(), name='create_category'),
    path('category/update/<str:slug>/', views.UpdateCategory.as_view(), name='update_category'),
    path('category/delete/<str:slug>/', views.DeleteCategory.as_view(), name='update_category'),
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('pagination/products/', views.ProductsListPaginationView.as_view(), name='products_list'),
    path('product/create/', views.ProductCreate.as_view(), name='products_create'),
    path('product/<str:slug>/', views.ProductDetaiView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.ProductByCategory.as_view(), name='category_products'),
    path('product/delete/<str:slug>/', views.ProductDelete.as_view(), name='product_delete'),
    path('product/update/<str:slug>/', views.ProductUpdate.as_view(), name='product_update'),
]