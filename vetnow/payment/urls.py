from django.urls import path
from azbankgateways.urls import az_bank_gateways_urls
from . import views

urlpatterns = (
    path('bankgateways/', az_bank_gateways_urls()),
    # buying payments
    path('goto_gateway/', views.GoToGateWay.as_view()),
    path('callback-gateway/', views.VerifyFromGateWay.as_view(), name='call_back_gt'),
    # wallet payments
    path('goto_gateway-wallet/', views.GoToGateWayWallet.as_view()),
    path('callback-gateway-wallet/<str:usr>/<int:amount>/', views.VerifyFromGateWayWallet.as_view(), name='call_back_gt_wallet'),
    path('verify_for_cart/', views.VerifyToSendCart.as_view(), name='verify_for_cart'),
    path('api/v1/buying_w_wallet/', views.BuyingWithWallet.as_view(), name='buying_wallet'),
    path('api/v1/update_wallet/', views.UpdateUserWalletAfterBuying.as_view(), name='update_wallet_after_buying'),
)