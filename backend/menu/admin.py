from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
      'id',
      'name',
      'base_price',
      'current_price',
      'demand_score',
      'total_orders',
      'is_available',
    )

    search_fields = ('name',)