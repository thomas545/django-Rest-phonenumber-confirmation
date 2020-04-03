from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, permissions, views, exceptions
from rest_framework.response import Response
from phonenumber_confirmation.serializers import PhoneNumberSerializer, PINConfirmationSerializer
from phonenumber_confirmation.models import PhoneNumber, PhoneNumberConfirmation


class PhoneNumberView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get('phone', None)
        phone_number = PhoneNumber.objects.create(user=request.user,
                                                  phone=phone)
        confirmation = PhoneNumberConfirmation().create(phone_number)
        confirmation.send_confirmation()
        return Response({"pin": confirmation.pin})


class PINConfirmationView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get_object(self, serializer):
        instance = get_object_or_404(PhoneNumberConfirmation,
                                     pin=serializer.validated_data.get(
                                         'pin', None))
        return instance

    def get_serializer(self, *args, **kwargs):
        return PINConfirmationSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pin = serializer.validated_data.get('pin', None)
        confirmation = self.get_object(serializer)
        confirmation.confirmation(pin)
        return Response({"detail": _("Phone number verified.")})


class ResendConfirmationView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, phonenumber_id, *args, **kwargs):
        try:
            confirm = PhoneNumberConfirmation.objects.get(
                phone_number__id=phonenumber_id)
            confirm.resend_confirmation()
        except PhoneNumberConfirmation.DoesNotExist:
            raise exceptions.NotAcceptable(_("Phone number not found."))
        return Response({"detail": _("Pin successfully resend.")})
