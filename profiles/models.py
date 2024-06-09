from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from products.models import Product


class Profile(models.Model):
    """
    Represents a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the Profile model.
        """
        return f'{self.user.username}\'s profile'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile.
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


class Review(models.Model):
    """
    Represents a review for a product written by a user profile.
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the Review model.
        """
        return f'Review for {self.product.name} by {self.user_profile.user.username}'


class Rating(models.Model):
    """
    Represents a rating given to a product review
    ranging from 1 to 5 stars.
    """

    review = models.OneToOneField(
        'Review', on_delete=models.CASCADE, related_name='rating')
    score = models.IntegerField(
        help_text="Rate the product from 1 to 5 stars",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

    def __str__(self):
        """
        Return a string representation of the Rating model.
        """
        return f'{self.score} Stars - {self.review.product.name} by {self.review.user_profile.user.username}'


class Wishlist(models.Model):
    """
    Represents a wishlist item for a user in the application.
    """
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wishlist_items')

    def __str__(self):
        """
        Return a string representation of the Wishlist model.
        """
        return f"{self.user_profile.user.username}'s wishlist - {self.product.name}"
