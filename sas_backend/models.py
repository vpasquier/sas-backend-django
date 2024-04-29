from django.contrib.auth.models import User
from django.db import models


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.TextChoices("Rating", "1 2 3 4 5")
    avatar = models.ImageField(default="", upload_to="profile_images")
    bio = models.TextField()

    def __str__(self):
        return self.user.username


# Booking object
class Booking(models.Model):
    make_up = models.BooleanField(default=False, blank=True)
    wig = models.BooleanField(default=False, blank=True)
    clothes = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    status = models.TextChoices("Status", "PENDING CANCELLED ACCEPTED REJECTED")
    designer = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="designer"
    )
    customer = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="customer"
    )
    location = models.CharField(max_length=180)
    comment = models.CharField(max_length=180, blank=True, null=True)
    price = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.session


# Customer cart
class Cart(models.Model):
    sessions = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)


# Designer offer
class Offer(models.Model):
    wig_price = models.FloatField(default=0, blank=True)
    clothes_price = models.FloatField(default=0, blank=True)
    make_up_price = models.FloatField(default=0, blank=True)
    designer = models.OneToOneField(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=180, blank=True, null=True)


# Notification object
class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=180, blank=True, null=True)
    read = models.BooleanField(default=False)
