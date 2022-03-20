from django.urls import path
from azbankgateways.urls import az_bank_gateways_urls
from . import views

urlpatterns = (
    path('bankgateways/', az_bank_gateways_urls()),
    path('goto_gateway/<int:payment>/', views.GoToGateWay.as_view()),
    path('callback-gateway/', views.VerifyFromGateWay.as_view(), name='call_back_gt'),
    path('verify_for_cart/', views.VerifyToSendCart.as_view(), name='verify_for_cart'),
)