# Generated by Django 4.2.10 on 2024-06-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_email',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='default_fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]