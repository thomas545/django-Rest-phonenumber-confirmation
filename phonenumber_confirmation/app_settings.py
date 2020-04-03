from django.conf import settings




UNIQUE_PHONE_NUMBER = getattr(settings, 'UNIQUE_PHONE_NUMBER', True)
PHONE_CONFIRMATION_EXPIRE_MINUTES = getattr(settings, 'PHONE_CONFIRMATION_EXPIRE_MINUTES', 15)
