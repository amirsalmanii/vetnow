from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('otp/verify/', views.UserVerifyAndOtp.as_view(), name='verify_by_otp'),
    path('otp/confirm/', views.UserConfirmOtp.as_view(), name='confirm_after_verify'),
    path('user/register/', views.UserRegisterView.as_view(), name='user_register'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
]