# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)  # Assuming image URLs are stored as strings

class ProductVariant(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
