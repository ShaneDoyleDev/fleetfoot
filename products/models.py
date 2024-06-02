from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from products.utils import set_upload_path


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
