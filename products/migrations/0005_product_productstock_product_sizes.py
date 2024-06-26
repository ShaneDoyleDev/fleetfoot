# Generated by Django 4.2.10 on 2024-06-02 12:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('on_sale', models.BooleanField(default=False)),
                ('sale_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.utils.set_upload_path)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.brand')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.department')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.shoetype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0, help_text='Stock level cannot be below 0', validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stocks', to='products.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stocks', to='products.size')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(related_name='products', through='products.ProductStock', to='products.size'),
        ),
    ]
