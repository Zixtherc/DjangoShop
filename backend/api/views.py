from rest_framework.viewsets import ModelViewSet
from products.models import Product
from order.models import Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer