from django.urls import path
from . import views


urlpatterns = [
    path('categoies/', views.CategoriesView.as_view(), name='send_categories')
]