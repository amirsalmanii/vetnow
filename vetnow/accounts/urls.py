from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('otp/verify/', views.UserVerifyAndOtp.as_view(), name='verify_by_otp'),
    path('otp/confirm/', views.UserConfirmOtp.as_view(), name='confirm_after_verify'),
    path('user/register/', views.UserRegisterView.as_view(), name='user_register'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/list/', views.UserListView.as_view(), name='users_list'),
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/count/', views.UsersCountView.as_view(), name='user_count'),
    path('profile/update/', views.UserDetailForUserProfileView.as_view(), name='profile_update'),
    path('check/user/per/', views.IsAdmin.as_view(), name='user_check'),
]