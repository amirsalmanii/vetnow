from django.contrib import admin
from .models import UserOtp
from rest_framework.authtoken.models import Token

admin.site.register(UserOtp)
admin.site.register(Token)
