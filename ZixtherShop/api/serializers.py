from rest_framework import serializers
from products.models import Product
from order.models import Order, OrderItem

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    user = serializers.CharField('phone_number.') # thinking
