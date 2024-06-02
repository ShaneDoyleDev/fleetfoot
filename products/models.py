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
