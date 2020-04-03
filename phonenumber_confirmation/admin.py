from django.contrib import admin
from .models import PhoneNumber, PhoneNumberConfirmation



class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user', 'primary', 'verified')
    list_filter = ('primary', 'verified')
    raw_id_fields = ('user',)


class PhoneNumberConfirmationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'sent', 'pin')
    list_filter = ('sent',)
    raw_id_fields = ('phone_number',)


admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(PhoneNumberConfirmation, PhoneNumberConfirmationAdmin)