import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.PositiveIntegerField(blank=False, null=False, db_index=True)
    supplier = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=127, blank=True, null=True)
    review_rating = models.CharField(max_length=5)
    price = models.FloatField(blank=True, null=True)
    total_quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
