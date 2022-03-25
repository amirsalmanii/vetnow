import logging
from django.shortcuts import redirect
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from accounts.models import User

class GoToGateWay(APIView):
    def post(self, request):
        serializer = serializers.TotalPriceSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['total_price']
            user_mobile_number = request.user
        else:
            return Response(serializer.errors, status=400)
        factory = bankfactories.BankFactory()
        try:
            bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount)

            bank.set_client_callback_url(reverse('call_back_gt'))
            bank.set_mobile_number(user_mobile_number)


            bank_record = bank.ready()

            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e
    

class VerifyFromGateWay(APIView):
    def get(self, request):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')

        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')

        if bank_record.is_success:
            return redirect(f'http://45.159.113.83:3010/payments/successful?tc={tracking_code}')
        

        # وقتی در راه اشتباهی میشه و پول گم بشه در چهل و هشت ساعت برمیگرده یا انصراف زدن
        return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')


class VerifyToSendCart(APIView):
    def post(self, request):
        serializer = serializers.VerifyToCartSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                result = bank_models.Bank.objects.get(tracking_code=data['tracking_code'])
            except:
                return Response(False, status=400)
            else:
                if result.status == 'Complete':
                    result.status = 'Expire verify payment' # means verifyed
                    result.save()
                    return Response(True, status=200)
                return Response(False, status=400)
        return Response(serializer.errors, status=400)


# wallet payment

class GoToGateWayWallet(APIView):
    def post(self, request):
        serializer = serializers.TotalPriceSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['total_price']
            user_mobile_number = request.user
        else:
            return Response(serializer.errors, status=400)
        factory = bankfactories.BankFactory()
        try:
            bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount)

            bank.set_client_callback_url(reverse('call_back_gt_wallet', args=[request.user, amount]))
            bank.set_mobile_number(user_mobile_number)


            bank_record = bank.ready()

            # return Response('yes')
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e


class VerifyFromGateWayWallet(APIView):
    def get(self, request, usr, amount):
        try:
            user = User.objects.get(username=usr) # who added to him wallet
        except:
            pass
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')

        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')

        if bank_record.is_success:
            user.wallet += amount
            user.save()
            return redirect(f'http://45.159.113.83:3010/payments/walletSuccessful?tc={tracking_code}')


        # وقتی در راه اشتباهی میشه و پول گم بشه در چهل و هشت ساعت برمیگرده یا انصراف زدن
        return redirect(f'http://45.159.113.83:3010/payments/failed?tc={tracking_code}')


class BuyingWithWallet(APIView):
    def get(self, request):
        return Response(request.user.wallet, status=200)


class UpdateUserWalletAfterBuying(APIView):
    def post(self, request):
        serializer = serializers.TotalPriceSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            amount = serializer.validated_data['total_price']
            user.wallet = amount
            user.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)
            
