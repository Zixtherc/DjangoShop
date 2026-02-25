from rest_framework import serializers
from products.models import Product
from order.models import Order, OrderItem

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()

    def info_product(self):
        data = getattr(self, 'validated_data', None)
        if data:
            return data['name'], data['description'], data['price'], data['stock']
        return data['name'], data['description'], data['price'], data['stock']

class OrderSerializer(serializers.Serializer):
    user = serializers.CharField(source= 'user.email', read_only = True)
    created_at = serializers.DateTimeField(read_only = True)
    status = serializers.CharField(max_length=20, default='new')

    def info_order(self):
        data = getattr(self,'validated_data', None)
        if data:
            return data['user']['email'], data['created_at'], data['status']

class OrderItemSerializer(serializers.Serializer):
    order = serializers.IntegerField(source= 'order.id', read_only=True)
    product = serializers.IntegerField(source= 'product.id', read_only= True)
    quantity = serializers.IntegerField(default= 1) 

    def info_order(self):
        data = getattr(self,'validated_data', None)
        if data:
            return data['order'], data['product'], data['quantity']