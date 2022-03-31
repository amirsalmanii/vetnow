from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('orders/', views.OrdersView.as_view(), name='orders_list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='orders_create'),
    path('orders/item/create/', views.OrderItemsCreateView.as_view(), name='orders_items'),
    path('orders/<int:pk>/<str:order_id>/', views.OrderUpdateView.as_view(), name='orders_update'),
    path('orders/status/count/', views.OrdersStatusCountView.as_view(), name='orders_status_count'),
    path('refunds/', views.RefundsOrdersRequestView.as_view(), name='refunds'),
    path('refund/<int:pk>/', views.RefundOrderRequestDetailView.as_view(), name='refunds_detail'),
    path('refund/create/', views.RefundCreateView.as_view(), name='refunds_create'),
    path('refund/update/<int:pk>/', views.RefundOrderRequestUpdateView.as_view(), name='refunds_update'),
    # users
    path('user/orders/', views.UserOrders2View.as_view(), name='orders_users_list'),
    path('user/order/<str:order_id>/', views.OrderUserUpdateView.as_view(), name='order_user_detail'),
]