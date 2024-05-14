import os

import pytest
from django.test import TestCase
from factories import BookingFactory


@pytest.fixture(scope="session", autouse=True)
def init():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sas-backend.settings")


class BookingTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        booking = BookingFactory()
        self.assertEqual(str(booking), booking.comment)
