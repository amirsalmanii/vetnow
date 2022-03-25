<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView


class GoToGateWay(APIView):
    def get(self, request, payment):
        amount = payment
        user_mobile_number = '09914342975'

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
            logging.debug("ﺎﯿﻧ ﻞﯿﻨﮐ ﻢﻌﺘﺑﺭ ﻦﯿﺴﺗ.")
            raise Http404

        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            logging.debug("ﺎﯿﻧ ﻞﯿﻨﮐ ﻢﻌﺘﺑﺭ ﻦﯿﺴﺗ.")
            raise Http404

        if bank_record.is_success:
            return HttpResponse("ﭖﺭﺩﺎﺨﺗ ﺏﺍ ﻡﻮﻔﻘﯿﺗ ﺎﻨﺟﺎﻣ ﺵﺩ.")

        return HttpResponse("ﭖﺭﺩﺎﺨﺗ ﺏﺍ ﺶﮑﺴﺗ ﻡﻭﺎﺠﻫ ﺵﺪﻫ ﺎﺴﺗ. ﺎﮔﺭ ﭖﻮﻟ ﮏﻣ ﺵﺪﻫ ﺎﺴﺗ ﻅﺮﻓ ﻡﺪﺗ ۴۸ ﺱﺎﻌﺗ ﭖﻮﻟ ﺐﻫ ﺢﺳﺎﺑ ﺶﻣﺍ ﺏﺍﺰﺧﻭﺎﻫﺩ ﮓﺸﺗ.")
>>>>>>> c68c5d5f86f2a266cc6ea9d467b14535e98669ad
