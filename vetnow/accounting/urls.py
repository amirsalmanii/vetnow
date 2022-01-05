from django.urls import path
from . import views

urlpatterns = [
    path('gains/<str:slug>/', views.ComputeGain.as_view(), name='categories_gains'),
    path('gains/', views.ComputeGainWithTime.as_view(), name='gains_by_date'),
    path('orders_count/', views.AllOdersCountView.as_view(), name='all_orders_count'),
    path('total_gains/', views.TotalCategoryGainsView.as_view(), name='total_gains')
]