from rest_framework.generics import ListAPIView
from .models import Dish
from .serializers import DishSerializer


class DishListAPIView(ListAPIView):
    queryset = Dish.objects.filter(is_available=True)
    serializer_class = DishSerializer