from django.db import models
from decimal import Decimal

class Dish(models.Model):
    name = models.CharField(max_length=255)

    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    demand_score = models.IntegerField(default=0)

    min_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('50.00')
    )

    max_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('1000.00')
    )

    total_orders = models.IntegerField(default=0)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{self.name} - ₹{self.current_price}"