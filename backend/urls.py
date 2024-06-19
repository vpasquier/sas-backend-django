from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from sas_backend import views

router = routers.DefaultRouter()
router.register(r"offers", views.OfferView, "offer")
router.register(r"profiles", views.ProfileView, "profile")
router.register(r"bookings", views.BookingView, "booking")
router.register(r"carts", views.CartView, "cart")
router.register(r"notifications", views.NotificationView, "notification")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("yo/", views.CustomEndpoint.as_view(), name="mycustom"),
    path("silk/", include("silk.urls", namespace="silk")),
]
