from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from products.validators import validate_non_negative


class Department(models.Model):
    """
    Model representing a department for the store.
    """
    name = models.CharField(max_length=20, unique=True)
    friendly_url_name = models.SlugField(unique=True)


class ShoeType(models.Model):
    """
    Model representing a specific type of shoe.
    """
    name = models.CharField(max_length=20, unique=True)
    friendly_url_name = models.SlugField(unique=True)


class Brand(models.Model):
    """
    Model representing a product's brand.
    """
    name = models.CharField(max_length=50, unique=True)
    friendly_url_name = models.SlugField(unique=True)


class Product(models.Model):
    """
    Model representing a product in the store.
    """
    sku = models.CharField(
        max_length=100,
        unique=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT
    )
    shoe_type = models.ForeignKey(
        ShoeType,
        on_delete=models.PROTECT
    )
    list_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[validate_non_negative]
    )
    on_sale = models.BooleanField(default=False)
    sale_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validate_non_negative],
        null=True,
        blank=True
    )
    current_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    sizes = models.ManyToManyField(
        'Size',
        through='ProductStock',
        related_name='products'
    )
    image = models.ImageField(
        upload_to='media/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        Return a string representation of the Product model.
        """
        return self.name

    def is_available(self):
        """
        Checks if the product is available.
        """
        return self.product_stocks.filter(stock__gt=0).exists()

    def get_image_url(self):
        """
        If the product has an image and the image has a URL, the URL is returned.
        Otherwise, a default image URL is returned.
        """
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/no-image.webp'

    def save(self, *args, **kwargs):
        """
        Save the product instance.

        If the product is on sale and a sale percentage is provided,
        calculate the discount and update the current price accordingly.
        Otherwise, set the current price to be equal to the list price.
        """
        if self.on_sale and self.sale_percentage is not None:
            discount = self.list_price * \
                (self.sale_percentage / Decimal('100'))
            self.current_price = self.list_price - discount
        else:
            self.current_price = self.list_price
        super().save(*args, **kwargs)


class Size(models.Model):
    """
    Model representing a sizing for an individual product.
    """
    size = models.CharField(max_length=5)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT
    )

    def __str__(self):
        """
        Return a string representation of the Size model.
        """
        return f"{self.department.name} Size {self.size}"


class ProductStock(models.Model):
    """
    Model representing the stock level of a
    product in a specific size.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_stocks'
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='product_stocks'
    )
    stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Stock level cannot be below 0"
    )

    def __str__(self):
        """
        Returns a string representation of the ProductStock model.
        """
        return (f"{self.product.name} - {self.size.size} "
                f": {self.stock} units available")

    def clean(self):
        """
        Validates that the size department
        matches the product department.
        Raises a ValidationError if they do not match.
        """
        if self.size.department != self.product.department:
            raise ValidationError(
                f"Size department '{self.size.department}' "
                f"does not match product department '{
                    self.product.department}'."
            )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to run validation before saving.
        """
        self.clean()
        super().save(*args, **kwargs)
