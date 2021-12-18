from rest_framework import serializers
from .models import User
from otp.models import UserOtp
from datetime import timedelta
from django.utils import timezone


class OtpVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, allow_null=False)

    def validate_phone_number(self, value):
        """
        check we have this number in system.
        """
        is_exists = User.objects.filter(username=value).exists()
        if is_exists:
            return value
        else:
            raise serializers.ValidationError("این شماره موبایل در سیستم ثبت نشده است")


class OtpConfirmSerializer(serializers.Serializer):
    key = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False, allow_blank=False)

    def validate(self, data):
        """
        Check that password is correct .
        """

        otp_obj = UserOtp.objects.filter(key=data['key'])
        if otp_obj:
            otp_obj = otp_obj.first()

            # compute the (datatime created + 2 min) is lower than when requested password now
            create_time = otp_obj.created_at
            create_time_plus_2_min = timedelta(minutes=2) + create_time
            now = timezone.now()
            if now > create_time_plus_2_min:
                raise serializers.ValidationError('بیشتر از دو دقیقه از ارسال این کد گذشته است لطفا دوباره امتحان کنید')
            if data['password'] == otp_obj.password:
                data['phone_number'] = otp_obj.phone_number
                return data
            else:
                raise serializers.ValidationError('رمز وارد شده اشتباه می باشد')
        else:
            pass  # alwase we have key because backend sent to front end correctly.


class UserRegisterSerilizer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, allow_null=False, allow_blank=False)

    def validate_phone_number(self, value):
        """
        check this number valid in iran system [valid number in iran --> 09148856432]
        """
        if '0' in value[0] and '9' in value[1]:
            return value
        else:
            raise serializers.ValidationError("شماره وارده استندارد نمی باشد")


class UserUpdateSerilizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "avatar",
            "national_code",
            "job",
            "graduate",
            "experience",
            "doctorDescreption",
            "doctorId",
            # address fields
            "state",
            "city",
            "address",
            "plate",
            "zip_code",
            "full_name",
            "phone_number",
        )

