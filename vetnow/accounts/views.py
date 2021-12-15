from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from otp.models import UserOtp
from kavenegar import *
from django.conf import settings
from rest_framework.authtoken.models import Token
from .models import User


class UserVerifyAndOtp(APIView):
    def post(self, request):
        serializer = serializers.OtpVerifySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            otp_obj = UserOtp.objects.save_data_otp(data)
            try:
                api = KavenegarAPI(settings.API_KEY)
                msg = str(otp_obj.password) + '----کد را برای احراز هویت وارد کنید----'
                params = {
                    'sender': '',  # optional
                    'receptor': otp_obj.phone_number,
                    'message': msg,
                }
                response = api.sms_send(params)
            except APIException as e:
                pass
            except HTTPException as e:
                pass
            return Response({"key": otp_obj.key}, status=200)

        return Response(serializer.errors, status=404)


class UserConfirmOtp(APIView):
    def post(self, request):
        serializer = serializers.OtpConfirmSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = User.objects.get(username=data['phone_number'])
            token = Token.objects.filter(user=user)
            if token:
                token = token.first()
                return Response({"token": token.key}, status=200)
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=200)
        return Response(serializer.errors, status=404)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = serializers.UserRegisterSerilizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            username = data['phone_number']
            user = User(username=username)
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response(serializer.errors, status=401)


class UserUpdateView(APIView):
    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = serializers.UserUpdateSerilizer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)
