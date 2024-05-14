from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView

from .models import Booking, Cart, Notification, Offer, Profile
from .serializers import (
    BookingSerializer,
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
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class NotificationView(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class CustomEndpoint(APIView):
    def get(self, request):
        example = request.query_params.get("example")
        if not example:
            example = "vlad"
        return JsonResponse({"example": example}, status=status.HTTP_200_OK)
