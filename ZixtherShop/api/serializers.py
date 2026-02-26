from rest_framework import serializers
from products.models import Product
from order.models import Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
        ]
    
    def validate_stock(self,value):
        if value < 0:
            raise serializers.ValidationError('Stock cannot be negative.')
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )
    product_price = serializers.DecimalField(
        source="product.price",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            'description',
            "product_price",
            "quantity",
        ]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    user_email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user_email",
            "created_at",
            "status",
            "items",
        ]