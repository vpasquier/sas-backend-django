from django.test import TestCase
from factories import BookingFactory
from serializers import BookingSerializer


class BookingTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        booking = BookingFactory()
        self.assertEqual(
            str(booking), f"Booking of {booking.customer} with {booking.designer}"
        )


class BookingTestSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        booking = BookingFactory()
        serializer = BookingSerializer(booking)
        for field_name in [
            "id",
            "location",
            "comment",
            "designer",
            "wig",
            "make_up",
            "clothes",
            "customer",
        ]:
            self.assertEqual(serializer.data[field_name], getattr(booking, field_name))
