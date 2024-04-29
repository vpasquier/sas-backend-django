from django.contrib import admin

from sas_backend.models import Booking, Cart, Notification, Offer, Profile

# Register your models here.

admin.site.register(Booking)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Offer)
