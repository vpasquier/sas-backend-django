from rest_framework import viewsets

from .models import Booking, Cart, Notification, Offer, Profile
from .serializers import (
    BookingSerialier,
    CartSerializer,
    NotificationSerializer,
    OfferSerializer,
    ProfileSerializer,
)


class OfferView(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerialier
    queryset = Booking.objects.all()


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class NotificationView(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
