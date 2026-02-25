from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', viewset=ProductViewSet)
router.register(r'orders', viewset=OrderViewSet)