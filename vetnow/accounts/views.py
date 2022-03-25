from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import serializers
from rest_framework.response import Response
from otp.models import UserOtp
from kavenegar import *
# from django.conf import settings
from config import secret
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework.pagination import PageNumberPagination
from ip2geotools.databases.noncommercial import DbIpCity
from accounts.models import IpTables
from rest_framework import filters



class MyPagination(PageNumberPagination):
    page_size = 20


class UserVerifyAndOtp(APIView):
    def post(self, request):
        serializer = serializers.OtpVerifySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            otp_obj = UserOtp.objects.save_data_otp(data)
            try:
                api = KavenegarAPI(secret.K_API_KEY)
                msg = str(otp_obj.password)
                params = {
                    'receptor': otp_obj.phone_number,
                    'template': 'verifyvetnow',
                    'token': msg,
                    'type': 'sms',
                }   
                response = api.verify_lookup(params)
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
            if user.is_admin:
                admin=True
            else:
                admin=False
            token = Token.objects.filter(user=user)
            otps = UserOtp.objects.filter(phone_number=user).delete()
            if token:
                token = token.first()
            else:
                token = Token.objects.create(user=user)
            return Response({"token": token.key, 'admin': admin}, status=200)
        else:
            return Response(serializer.errors, status=404)


class UserDeleteView(APIView):
    permission_classes = (IsAdminUser,)
    def delete(self, request, pk):
        try:
            usr = User.objects.get(id=pk)
        except:
            return Response(status=404)
        else:
            usr.delete()
            return Response(status=204)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = serializers.UserRegisterSerilizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            username = data['phone_number']
            usr = User.objects.filter(username = username)
            if not usr:
                user = User(username=username)
                user.save()
                token = Token.objects.create(user=user)
            else:
                return Response('کاربر قبلا ثبت شده است', status=404)
            return Response({"token": token.key}, status=200)
        else:
            return Response(serializer.errors, status=401)


class UserUpdateView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = serializers.UserListSerializer(user, context={'request': request})
        return Response(serializer.data, status=200)
        
    def put(self, request, pk):# TODO: use try exept
        user = User.objects.get(id=pk)
        serializer = serializers.UserUpdateSerilizer(instance=user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors)


class UserListView(ListAPIView):
    permission_classes = (IsAdminUser,) 
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name', 'national_code']
    

class UserCreateView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer


class UsersCountView(APIView):
    def get(self, request):
        users = User.objects.all().count()
        return Response({'users_count': users}, status=200)


class IsAdmin(APIView):
    """
    checker for user is admin or not for admin panel
    """
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_admin:
                return Response({'is_admin': True}, status=200)
            else:
                return Response({'is_admin': False}, status=200)
        else:
            return Response({'login': False})


class UserDetailForUserProfileView(APIView):
    """
    update owen profile information
    """
    def get(self, request):
        username = request.user
        try:
            user = User.objects.get(username=username)
        except:
            return Response("user not found", status=404)
        else:
            serializer = serializers.UserProfileUpdate(user, context={'request': request})
            return Response(serializer.data, status=200)
    
    def put(self, request):
        username = request.user
        try:
            user = User.objects.get(username=username)
        except:
            return Response("user not found", status=404)
        else:
            serializer = serializers.UserProfileUpdate(instance=user, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)


class UserWalletView(APIView):
    """
    update or read user wallet
    """
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        wallet = request.user.wallet
        return Response({'wallet': wallet})

    def put(self, request):
        username = request.user
        try:
            user = User.objects.get(username=username)
        except:
            return Response("user not found", status=404)
        else:
            serializer = serializers.UserWalletSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                valid_data = serializer.validated_data['wallet']
                valid_data += user.wallet
                user.wallet = valid_data
                user.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
