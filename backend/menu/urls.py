from django.urls import path
from .views import DishListAPIView

urlpatterns = [
    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
]