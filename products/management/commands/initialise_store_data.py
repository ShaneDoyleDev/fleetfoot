from django.core.management import call_command
from django.core.management.base import BaseCommand
from products.models import Product, Size, ProductStock
import random


class Command(BaseCommand):
    help = ('''Load the product data and populate
    the database with random stock levels
    for different sizes for each shoe.''')

    def handle(self, *args, **kwargs):
        # Reset database to prevent entry of duplicate values
        call_command('flush', '--noinput')
        self.stdout.write(self.style.SUCCESS(
            'Database successfully reset!'))

        # List of fixture files
        fixture_files = [
            'department_fixtures.json',
            'brand_fixtures.json',
            'shoe_type_fixtures.json',
            'size_fixtures.json',
            'mens_product_fixtures.json',
            'womens_product_fixtures.json',
            'kids_products_fixtures.json',
        ]

        # Load each fixture
        for fixture_file in fixture_files:
            try:
                call_command(
                    'loaddata',
                    fixture_file,
                    app_label='products'
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully loaded {fixture_file}!'
                    ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'An error occurred while loading {fixture_file}: {str(e)}'
                ))

        products = Product.objects.all()
        sizes = Size.objects.all()

        for product in products:
            # Call save method to ensure product's current price field is calculated
            product.save()

            matching_sizes = sizes.filter(
                department=product.department
            )
            for size in matching_sizes:
                # Generate a random stock level between 0 and 100
                stock_level = random.randint(0, 100)
                ProductStock.objects.create(
                    product=product,
                    size=size,
                    stock=stock_level
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created stock for {
                            product.name} - {size.department} Size {size.size}: {stock_level} units'
                    )
                )

        # After loading fixtures and creating ProductStock instances
        for product in products:
            product.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Saved product {product.name} to update current_price'
                )
            )

        self.stdout.write(self.style.SUCCESS(
            "Database successfully populated " +
            "with initial data!"
        ))
