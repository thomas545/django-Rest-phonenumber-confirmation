from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_confirmation.fields import PhoneNumberSerializerField
from .models import PhoneNumber, PhoneNumberConfirmation


class PhoneNumberSerializer(serializers.Serializer):
    phone = PhoneNumberSerializerField()      

    def validate(self, data):
        if PhoneNumber.objects.filter(phone=data.get('phone', '')):
            raise serializers.ValidationError(_("A user use this phone number before.")) 
        return data


class PINConfirmationSerializer(serializers.Serializer):
    pin = serializers.IntegerField()     

    def validate(self, data):
        if not PhoneNumberConfirmation.objects.filter(pin=data.get('pin', '')):
            raise serializers.ValidationError(_("Wrong pin."))
        return data

