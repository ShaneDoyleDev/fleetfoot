from django import template

register = template.Library()


@register.filter
def times(number):
    """
    Returns a range object that represents a sequence
    of numbers from 0 up to (but not including) the given number.
    """
    return range(number)
