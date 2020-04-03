from django.db import models


class PhoneNumberManager(models.Manager):
    def add_phone_number(self, user, phone, primary=False, confirm=False):
        phone_number, created = self.get_or_create(user=user,
                                                   phone=phone,
                                                   primary=primary)

        if created and confirm:
            phone.send(phone_number, confirm)
        return phone_number

    def get_primary(self, user):
        try:
            return self.get(user=user, primary=True)
        except self.model.DoesNotExist:
            return None
