from django.urls import path
from . import views


urlpatterns = [
    path('otp/verify/', views.UserVerifyAndOtp.as_view(), name='verify_by_otp'),
    path('otp/confirm/', views.UserConfirmOtp.as_view(), name='confirm_after_verify'),
]