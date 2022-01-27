from django.db import models
import uuid
from random import randrange


class OtpManager(models.Manager):
    def save_data_otp(self, data):
        phone = data['phone_number']
        password_random = randrange(1000, 9999)
        otp_obj = self.model(phone_number=phone, password=password_random)
        otp_obj.save()
        return otp_obj


class UserOtp(models.Model):
    key = models.UUIDField(default=uuid.uuid4)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = OtpManager()

    def __str__(self):
        return f'{self.id} -- {self.phone_number}'
    
    class Meta:
        ordering = ('-id',)
