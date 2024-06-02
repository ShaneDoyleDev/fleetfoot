import os


def set_upload_path(instance, filename):
    """
    Dynamically set the image upload path
    based on the product's department and name.
    """
    department = instance.department
    product_name = instance.name.replace(' ', '_')
    return f'product_images/{department}/{product_name}/{filename}'
