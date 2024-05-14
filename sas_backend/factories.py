from factory.django import DjangoModelFactory
from factory.faker import Faker

from sas_backend.models import Booking


class BookingFactory(DjangoModelFactory):
    class Meta:
        model = Booking

    make_up = Faker("boolean")
    wig = Faker("boolean")
    clothes = Faker("boolean")
    # location = Faker("new york")
    # comment = Faker("a comment")
    # designer = Faker("a designer")
    # customer = Faker("a customer")
    price = Faker("pyfloat")

    class Meta:
        model = Booking
