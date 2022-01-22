from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('orders/', views.OrdersView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', views.OrderUpdateView.as_view(), name='orders_update'),
    path('users/orders/<int:pk>/', views.UserOrdersView.as_view(), name='orders_users_list'),
    path('orders/status/count/', views.OrdersStatusCountView.as_view(), name='orders_status_count'),
]