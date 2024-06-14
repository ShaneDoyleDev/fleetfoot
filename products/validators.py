from django.core.exceptions import ValidationError
from decimal import Decimal


def validate_non_negative(value):
    """
    Validates that the given value is non-negative.
    """
    if value < Decimal('0.00'):
        raise ValidationError('Value cannot be negative.')
