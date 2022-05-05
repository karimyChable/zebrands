import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    sku = models.CharField(max_length=250, null=False, blank=False)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

